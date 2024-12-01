# --- Day 19: Aplenty ---
import os
from typing import Dict, List
from enum import Enum
DAY = "19"

# part 2
NodeType = Enum('NodeType', ['branch', 'leaf'])
Condition = Enum('Condition', ['gt', 'lt'])

class Branch:
    def __init__(self, condition: Condition, value: int):
        self.condition = condition
        self.value = value

class Node:
    def __init__(self, type: NodeType, *data):
        self.type = type
        match type:
            case 'branch':
                self.data = data
            case 'leaf':
                self.data = data[0]
        assert False
    
# def toGraph(workflow: Dict[str, List]):
#     tree = {}
#     stack = ['in']
#     while stack:
#         curr = stack.pop()
        
#     pass


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        workflowRaw, partsRaw = [d.split('\n')
                                 for d in document.read().split('\n\n')]
        workflow = [
            (s[:s.index('{')], s[s.index('{') + 1:-1].split(',')) for s in workflowRaw]
        parts = [[int(q[2:]) for q in p[1:-1].split(',')] for p in partsRaw]
        partsDict = [dict(zip(list('xmas'), part)) for part in parts]
        result = 0
        # for part in partsDict:
        #     if solve(dict(workflow), part) == 'A':
        #         result += sum(part.values())
        # print(result)
        print(dict(workflow))
