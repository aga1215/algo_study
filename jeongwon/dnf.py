# 시간복잡도: O(n log n)

from collections import deque
def solution(participant, completion):
    participant.sort()
    completion.sort()
    parts = deque(participant)
    comp = deque(completion)
    
    for i in range(len(comp)):
        x = parts.popleft()
        y = comp.popleft()
        if x != y:
            return x
    return parts[0]

