package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// recursion, either add or multiply an operand
func evaluate(curr int, operands []int, i int, target int) bool {
	if curr > target {
		return false
	}

	if i == len(operands) {
		return curr == target
	}

	add := evaluate(curr+operands[i], operands, i+1, target)
	multiply := evaluate(curr*operands[i], operands, i+1, target)

	return add || multiply
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
