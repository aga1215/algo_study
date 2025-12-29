'''
시간복잡도
이중 for문이지만 입력 범위가 1,000 이하의 자연수이기 때문에 1,000 * 1,000 = 100만 예측해봅니다..
'''

from collections import deque
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        temp = s[i:] + s[:i] # 회전시킨 문자열
        q = deque()
        for j in range(len(temp)): # 하나씩 q에 삽입
            if not q:
                q.append(temp[j])
            else: 
                if temp[j] == '[' or temp[j] == '{' or temp[j] == '(':
                    q.append(temp[j])
                elif temp[j] == ']' and q[-1] == '[':
                    q.pop()
                elif temp[j] == '}' and q[-1] == '{':
                    q.pop()
                elif temp[j] == ')' and q[-1] == '(':
                    q.pop()
         
        if not q:
            answer += 1

    return answer

# 입력 받기
temp = input()
for c in temp: 
    if c not in '{}[]()':
        break
print(solution(temp))

'''
개선: gpt 도움
- 괄호 쌍이 있기 때문에 딕셔너리 형태로 else 구문의 if 분기를 간결하게 작성할 수도 있음!

pairs = {']': '[', '}': '{', ')': '('}

for c in temp:
    if c in '([{':
        q.append(c)
    elif not q or q.pop() != pairs[c]:
        break

'''
