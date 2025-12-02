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
			// for a product id to be invalid, it should have even number of digits N
			// and left half = id // (10^0.5N) == id % (10^0.5N) = right half
			// we can easily determine N = floor(log10(id)) + 1
			N := int(math.Floor(math.Log10(float64(i))) + 1)
			halver := int(math.Pow10(N / 2))
			if N%2 == 0 && (i/halver) == i%halver {
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
