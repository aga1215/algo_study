from collections import deque

def solution(s):
    answer = 0
    s_deque = deque(s)
    
    for _ in range(len(s)):  # 1. 문자열의 길이만큼 회전하는 반복문
        stack = []  # 회전마다 스택 초기화
        ok = True   # 실패 여부 체크
        
        for i in range(len(s)):   # dq의 모든 자리를 돌며 괄호검사 로직
            if s_deque[i] in '({[':
                # 1-1. 해당 인덱스의 문자가 여는괄호 중 하나라면
                stack.append(s_deque[i]) # 스택에 해당 여는괄호 저장
            else:   # 1-2. 여는괄호가 아닌데,
                if not stack:   # 1-2-1. 스택 비었으면
                    ok = False
                    break
                    
                if s_deque[i] == ')' and stack[-1] == '(':
                    #1-2-2. 해당 인덱스의 문자가 닫는소괄호이고, 스택의 마지막 저장된 요소가 여는소괄호(짝)라면
                    stack.pop() # 스택에 저장된 여는소괄호 삭제
                elif s_deque[i] == '}' and stack[-1] == '{':
                    #1-2-3. 해당 인덱스의 문자가 닫는중괄호이고, 스택의 마지막 저장된 요소가 여는중괄호(짝)라면
                    stack.pop() # 스택에 저장된 여는중괄호 삭제
                elif s_deque[i] == ']' and stack[-1] == '[':
                    #1-2-4. 해당 인덱스의 문자가 닫는대괄호이고, 스택의 마지막 저장된 요소가 여는대괄호(짝)라면
                    stack.pop() # 스택에 저장된 여는대괄호 삭제
                else:   # 1-3. 짝이 안맞는 닫는괄호면
                    ok = False  # 실패
                    break
        # 2. 모든 자리 괄호 검사 후 ok=True이고, 스택이 비었다면(현재 dq는 모든 괄호 쌍인 문자열인 상태) answer+1 처리
        if ok and len(stack) == 0:
            answer += 1
        
        # 3. 맨앞거 빼서 맨뒤로 넣는 문자열 회전작업
        s_deque.rotate(-1)  # 왼쪽으로 1칸 회전(문제 조건)
        # print(s_deque)
        
    return answer