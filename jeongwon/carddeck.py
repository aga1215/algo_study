# 병합정렬의 느낌으로 둘 중 하나 맨 앞에가 goal에 있으면
from collections import deque
def solution(cards1, cards2, goal):
    ans = 'Yes'
    dq1 = deque(cards1)
    dq2 = deque(cards2)
    
    for item in goal:
        if len(dq1) > 0 and dq1[0] == item:
            dq1.popleft()
        elif len(dq2) > 0 and dq2[0] == item:
            dq2.popleft()
        else: 
            ans = 'No'
            break
    return ans
