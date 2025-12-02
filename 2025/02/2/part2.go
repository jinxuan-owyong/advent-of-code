package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type ProductRange struct {
	Start int
	End   int
}

func FindInvalidIDs(ranges []ProductRange) int {
	var total int
	for _, p := range ranges {
		for i := p.Start; i <= p.End; i++ {
			// for a product id to be invalid, number of digits N should be divisible by D < N
			// and each group of D digits should be the same, delimited by grouper = 10^(N/D)
			// we can easily determine N = floor(log10(id)) + 1
			N := int(math.Floor(math.Log10(float64(i))) + 1)
			found := false
			for D := 1; D <= N && !found; D++ {
				if N%D == 0 {
					grouper := int(math.Pow10(N / D))
					target := i % grouper
					temp := i
					for temp > 1 {
						if temp%grouper != target { // all groups should match target
							break
						}
						temp /= grouper // truncate right of temp by D digits
						if temp == target {
							found = true
							break
						}
					}
				}
			}
			if found {
				total += i
			}
		}
	}
	return total
}

func main() {
	var ranges []ProductRange
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		for r := range strings.SplitSeq(line, ",") {
			startEnd := strings.Split(r, "-")
			start, err := strconv.Atoi(startEnd[0])
			if err != nil {
				log.Panicf("invalid input %s", r)
			}
			end, err := strconv.Atoi(startEnd[1])
			if err != nil {
				log.Panicf("invalid input %s", r)
			}
			ranges = append(ranges, ProductRange{start, end})
		}
	}
	result := FindInvalidIDs(ranges)
	fmt.Println(result)
}
