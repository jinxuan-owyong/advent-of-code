# # --- Day 20: Pulse Propagation ---
# import os
# from typing import Dict, List
# from collections import defaultdict, deque
# DAY = "20"

# # part 1

# # sentLow = 0
# # sentHigh = 0

# # class FlipFlop:
# #     def __init__(self):
# #         self._state = False
# #     def update(self, pulse: bool) -> None:
# #         if pulse:
# #             return
# #         self._state = not self._state


# # class Conjunction:
# #     def __init__(self, inputNames: List[str]):
# #         self._state = dict(zip(inputNames, [False] * len(inputNames)))
# #         self._numHigh = 0
# #     def update(self, inputName: str, pulse: bool):
# #         if (self._state[inputName] and not pulse) or (not self._state[inputName] and pulse):
# #             self._numHigh += 1
# #         self._state[inputName] = pulse
# #     def getOutput(self):
# #         return not self._numHigh == len(self._state)
    
    
# # def solve(modules: Dict, outputs: Dict[str, List[str]], broadcast: List[str]):
# #     queue = deque()
# #     for _ in range(1):
# #         [queue.append((x, False)) for x in broadcast]
# #         while queue:
# #             id, pulse = queue.popleft()
# #             for output in outputs[id]:
                
# #             modules[id].update(pulse)
            


# if __name__ == "__main__":
#     with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
#         outputs = defaultdict(lambda: []) # outputs of flipflops and conjunctions
#         modules = {}
#         flipflops = []
#         conjunctions = []
#         broadcast = []
#         for line in document:
#             left, right = line.rstrip('\n').split(' -> ')
#             targets = right.split(', ')
#             match left[0]:
#                 case '%' | '&':
#                     id = left[1:]
#                     outputs[id].extend(targets)
#                     if left[0] == '%':
#                         flipflops.append(id)
#                         modules[id] = FlipFlop()
#                     else:
#                         conjunctions.append(id)
#                 case 'b':
#                     broadcast.extend(targets)
#         for cj in conjunctions:
#             modules[cj] = Conjunction(outputs[cj])
#         solve(modules, dict(outputs), broadcast)   
        