from collections import deque
def solution(s):
    answer = ''
    q = deque(s)
    # print(q)
    cnt = 0
    while q:
        x = q.popleft()
        if x == ' ':
            cnt = 0
            answer += x
            continue
        elif cnt % 2 == 0: 
            answer += x.upper()
        else: answer += x.lower()
        cnt += 1
    return answer
