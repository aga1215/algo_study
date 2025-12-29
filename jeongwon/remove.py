'''
시간복잡도: 100만 - for문 한 번 돌기 때문에
'''

from collections import deque
def solution(s):
    q = deque()
    for item in s:
        if not q: q.append(item)
        else: 
            if item == q[-1]:
                q.pop()
            else: q.append(item)
    return 0 if q else 1

# 입력받기
temp = input()
print(solution(temp))
