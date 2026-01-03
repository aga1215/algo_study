'''
시간복잡도: O(n)
입력: 10만
'''

from collections import deque
def solution(prices):
    time = [0] * len(prices)
    dq = deque()
    
    for i in range(len(prices)):
        while dq and prices[i] < prices[dq[-1]]: # 가격 하락 여부 확인
            time[dq[-1]] = abs(dq[-1] - i)
            dq.pop()
        dq.append(i)
    
    while dq: # 끝까지 안떨어졌다면?
        time[dq[-1]] = len(prices) - dq[-1] - 1
        dq.pop()
    return time

# 0 0 0 0 0 ... 이런 식으로 입력받기
arr = list(map, int(input().split))
solution(arr)
