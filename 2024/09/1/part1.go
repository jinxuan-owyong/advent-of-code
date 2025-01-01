package main

import (
	"bufio"
	"fmt"
	"os"
)

func compact(diskmap string) []int {
	var blocks []int // file ids
	id := 0
	for i, blockSize := range diskmap {
		f := -1
		if i%2 == 0 {
			f = id
			id += 1
		}
		for range int(blockSize) - int('0') {
			blocks = append(blocks, f)
		}
	}

	i := 0
	j := len(blocks) - 1
	for {
		// find next available free space
		for blocks[i] >= 0 {
			i += 1
		}
		// find next file to move
		for blocks[j] < 0 {
			j -= 1
		}
		if i >= j { // instead of for i < j, prevents last iteration from overshooting
			break
		}
		temp := blocks[i]
		blocks[i] = blocks[j]
		blocks[j] = temp
	}

	return blocks
}

func getChecksum(blocks []int) int {
	result := 0
	for i, id := range blocks {
		if id >= 0 {
			result += i * int(id)
		}
	}
	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	diskmap := scanner.Text()
	compacted := compact(diskmap)
	result := getChecksum(compacted)
	fmt.Println(result)
}
