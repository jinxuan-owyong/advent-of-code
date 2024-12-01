# --- Day 19: Aplenty ---
import os
from typing import Dict, List
DAY = "19"

# part 1


def solve(workflow: Dict[str, List], parts: Dict[str, int]):
    curr = 'in'
    while True:
        if curr in ('A', 'R'):
            return curr
        inst = workflow[curr]
        for step in inst:
            if step in ('A', 'R'):
                return step
            match step[1]:
                case '>':
                    left, right = step.split(':')
                    if parts[left[0]] > int(left[2:]):
                        curr = right
                        break
                case '<':
                    left, right = step.split(':')
                    if parts[left[0]] < int(left[2:]):
                        curr = right
                        break
                case _:
                    curr = step
                    break


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        workflowRaw, partsRaw = [d.split('\n')
                                 for d in document.read().split('\n\n')]
        workflow = [
            (s[:s.index('{')], s[s.index('{') + 1:-1].split(',')) for s in workflowRaw]
        parts = [[int(q[2:]) for q in p[1:-1].split(',')] for p in partsRaw]
        partsDict = [dict(zip(list('xmas'), part)) for part in parts]
        result = 0
        for part in partsDict:
            if solve(dict(workflow), part) == 'A':
                result += sum(part.values())
        print(result)
