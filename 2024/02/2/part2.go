package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"

	"github.com/samber/lo"
)

func evaluateSafety(levels []int) bool {
	var isIncreasing bool = true
	var isDecreasing bool = true

	i := 1
	for i < len(levels) && (isIncreasing || isDecreasing) {
		isIncreasing = isIncreasing && levels[i] > levels[i-1]
		isDecreasing = isDecreasing && levels[i] < levels[i-1]
		diff := math.Abs(float64(levels[i] - levels[i-1]))
		if diff < 1 || diff > 3 {
			return false
		}
		i += 1
	}

	return isIncreasing || isDecreasing
}

func removeIdx(arr []int, target int) []int {
	var removed []int
	for i := range len(arr) {
		if i != target {
			removed = append(removed, arr[i])
		}
	}
	return removed
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var result int = 0

	for scanner.Scan() {
		data := strings.Split(scanner.Text(), " ")
		levels := lo.Map(data, func(s string, _ int) int {
			return utils.ParseInt(s)
		})
		if evaluateSafety(levels) {
			result += 1
		} else {
			// brute force
			for skip := range len(levels) {
				if evaluateSafety(removeIdx(levels, skip)) {
					result += 1
					break
				}
			}
		}
	}

	fmt.Println(result)
}
