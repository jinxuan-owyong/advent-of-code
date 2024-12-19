package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func evaluate(curr int, operands []int, i int, target int) bool {
	if curr > target {
		return false
	}

	if i == len(operands) {
		return curr == target
	}

	add := evaluate(curr+operands[i], operands, i+1, target)
	mul := evaluate(curr*operands[i], operands, i+1, target)
	cat := false

	if i > 0 {
		var b strings.Builder
		b.WriteString(strconv.Itoa(curr))
		b.WriteString(strconv.Itoa(operands[i]))
		next, _ := strconv.Atoi(b.String())
		cat = evaluate(next, operands, i+1, target)
	}

	return add || mul || cat
}

func isPossibleResult(target int, operands []int) bool {
	return evaluate(operands[0], operands, 1, target)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	result := 0

	for scanner.Scan() {
		row := scanner.Text()
		sep := strings.Index(row, ":")
		calibrationResult, _ := strconv.Atoi(row[:sep])
		operands := utils.ParseArrInt(row[sep+2:], " ")
		if isPossibleResult(calibrationResult, operands) {
			result += calibrationResult
		}
	}

	fmt.Println(result)
}
