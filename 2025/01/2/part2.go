package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

const DialStart = 50
const DialSize = 100

func CalculatePassword(deltas []int) int {
	prev := DialStart
	curr := DialStart
	password := 0
	for _, d := range deltas {
		if math.Abs(float64(d)) > DialSize {
			password += int(math.Abs(float64(d)) / DialSize)
			d = d % DialSize
		}
		prev, curr = curr, curr+d
		if curr == 0 { // this check should be first, otherwise we will double count the zeros
			password += 1
		}
		if curr < 0 {
			curr += DialSize
			// need to keep track of prev since we do not count zeroes at the beginning of rotations
			if prev != 0 {
				password += 1
			}
		}
		if curr >= DialSize {
			curr -= DialSize
			if prev != 0 {
				password += 1
			}
		}
	}
	return password
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var deltas []int
	for scanner.Scan() {
		line := scanner.Text()
		multiplier := 1
		if line[0] == 'L' {
			multiplier = -1
		}
		num, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Panicf("invalid input %s", line)
		}
		deltas = append(deltas, multiplier*num)
	}
	result := CalculatePassword(deltas)
	fmt.Println(result)
}
