def solution(s:str): #s는 문자열
    s = list(s) #문자열을 리스트로 변환 
    answer = 0
    
    for i in range(len(s)):
        rotate_s = s[i:]+s[:i]
        stack = []
        
        for j in rotate_s:
            if len(stack) == 0:
                stack.append(j)
            else:
                if stack[-1] == '(' and j == ')':  #스택의 마지막 문자가 '('이고 현재 문자가 ')'라면
                    stack.pop() #스택의 마지막 문자 제거
                elif stack[-1] == '{' and j == '}':# 스택의 마지막 문자가 '{'이고, 현재 문자가'}'라면
                    stack.pop() #마지막 문자인 '{' 삭제
                elif stack[-1] == '[' and j == ']':
                    stack.pop()
                else:
                    stack.append(j)
        if len(stack) == 0:
            answer += 1
        
    return answer