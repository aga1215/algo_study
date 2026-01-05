"""
                    cur
prices = [100, 200, 300, 200, 300]
stack = [0, 1]  # 아직 가격이 떨어진 시점을 못 찾은 인덱스를 보관
top = 1
answer[i] = cur - i
이해가 안가네 이거 설명 해주실 분 계실까요?
"""

def solution(prices):
    n = len(prices)
    stack = []  # 아직 떨어진 시점을 못 찾은 인덱스 저장
    answer = [0] * n
    
#     1. prices만큼을 도는 외부 반복문
    for cur in range(n):
#         현재 가격이 더 낮아져서, 스택top의 가격이 '처음으로' 떨어졌다면 정답 확정
        while stack and prices[cur] < prices[stack[-1]]:
            i = stack.pop()
            answer[i] = cur - i
        stack.append(cur)
        
#     끝까지 안 떨어진 애들 처리
    last = n - 1
    while stack:
        i = stack.pop()
        answer[i] = last - i
    
    return answer