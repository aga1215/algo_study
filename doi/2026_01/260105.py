import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dq = deque(range(1, N+1))   # 1부터 N까지의 수 배열 생성
answer = []                 # 요세푸스 순열 저장할 배열

while dq:
    # print("dq:", dq)  # 현재 덱 상태 출력
    
    dq.rotate(-(K-1))    # K-1칸 왼쪽으로 회전
    answer.append(dq.popleft())  # 맨 앞의 원소 제거 후 요세푸스 순열에 추가
    
    # print("answer:", answer)  # 현재 요세푸스 순열 상태 출력
    
print("<" + ", ".join(map(str, answer)) + ">")