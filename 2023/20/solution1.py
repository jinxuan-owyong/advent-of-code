# --- Day 20: Pulse Propagation ---
import os
from typing import List, Tuple
from collections import defaultdict, deque
DAY = "20"

# part


def solve(flipflops: List[Tuple], conjunctions: List[Tuple], broadcast: List[str]):
    state = {}
    edgelist = defaultdict(lambda: [])
    for id, targets in flipflops:
        state[id] = False
        edgelist[id].extend(targets)
    
    for id, targets in conjunctions:
        state[id] = [False, 0]
        edgelist[id].extend(targets)
    
    for i in range(1):
        for b in broadcast:
            # button push flips state
            currB = state[b]
            state[b] = not state[b]
            newB = state[b]
            # update neighbours
            queue = deque()
            [queue.append(neighbour) for neighbour in edgelist[b]]
            while queue:
                curr = queue.popleft()
                if curr in conjunctions:
                    state[curr][2] += 1
                if state[curr][2] == len(edgelist[curr])
                
            pass

if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        lines = map(lambda x: x.rstrip('\n').split(' -> '), document)
        data = list(map(lambda x: (x[0], x[1].split(', ')), lines))
        flipflops = list(map(lambda x: (x[0][1:], x[1]), filter(lambda x: x[0][0] == '%', data)))
        conjunctions  = list(map(lambda x: (x[0][1:], x[1], 0), filter(lambda x: x[0][0] == '&', data)))
        broadcast = list(map(lambda x: x[1], filter(lambda x: x[0][0] == 'b', data)))
        solve(flipflops, conjunctions, broadcast)