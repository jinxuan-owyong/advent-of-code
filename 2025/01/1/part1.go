package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const DialStart = 50
const DialSize = 100

func CalculatePassword(deltas []int) int {
	curr := DialStart
	password := 0
	for _, d := range deltas {
		curr = (curr + d) % DialSize
		if curr < 0 {
			curr += DialSize
		}
		if curr == 0 {
			password += 1
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
