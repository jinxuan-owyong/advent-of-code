package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
)

func fillBlocks(blocks []int, i int, size int, val int) {
	for j := 0; j < size && i+j < len(blocks); j += 1 {
		blocks[i+j] = val
	}
}

func getNextAvailableFreeSpace(spaces []*binaryheap.Heap, requiredSize int) (int, int, bool) {
	lowest, idx := -1, int(1e10)
	// among the free spaces available, find the leftmost available space
	for size := requiredSize; size < len(spaces); size += 1 {
		top, ok := spaces[size].Peek()
		if ok && top.(int) < idx {
			lowest = size
			idx, _ = top.(int)
		}
	}
	// only pop from the leftmost heap after we scan through all potential heaps
	if lowest != -1 {
		spaces[lowest].Pop()
	}
	return lowest, idx, idx >= 0 && idx < int(1e10)
}

func compact(diskmap string) []int {
	var blocks []int // file ids
	// there are only 9 possible free space sizes
	var spaces = make([]*binaryheap.Heap, 10)
	for i := range 10 { // store the lowest index for a particular size free space
		spaces[i] = binaryheap.NewWithIntComparator()
	}

	id := 0
	for i, blockSize := range diskmap {
		f := -1
		size := int(blockSize) - int('0')
		if i%2 == 0 {
			f = id
			id += 1
		} else {
			spaces[size].Push(len(blocks))
		}
		for range size {
			blocks = append(blocks, f)
		}
	}

	j := len(blocks) - 1
	for {
		for j >= 0 && blocks[j] < 0 {
			j -= 1
		}
		i := j
		// find the next file block to move
		for i > 0 && blocks[i] == blocks[i-1] {
			i -= 1
		}
		if i == 0 {
			break
		}
		fileSize := j - i + 1
		freeSpaceSize, spaceStart, available := getNextAvailableFreeSpace(spaces, fileSize)
		// only move files forwards, and if it has not been moved
		if available && spaceStart < i {
			// add extra space remaining after moving file
			// don't need to account for original space occupied by file since we only move files to the left
			if freeSpaceSize > fileSize {
				spaces[freeSpaceSize-fileSize].Push(spaceStart + fileSize)
			}
			fillBlocks(blocks, spaceStart, fileSize, blocks[i])
			fillBlocks(blocks, i, fileSize, -1)
		}
		j = i - 1
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
	defragmented := compact(diskmap)
	result := getChecksum(defragmented) // > 6412358477900 && < 7089004792270
	fmt.Println(result)
}
