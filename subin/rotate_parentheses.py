#프로그래머스 괄호 회전 문제
#제한 조건 : s의 길이는 1 이상 1,000 이하입니다 ==> 입력값의 길이가 10000 이하 이므로 이중 반복문 사용
#해석 : 괄호의 올바름 확인 (안쪽 for문) > 괄호를 오른쪽으로 이동시켜 바뀐 괄호열을 확인 (바깥쪽 for문)
#시간복잡도 : O(n^2) - 이중 for문 사용했기 때문에


from collections import deque

# 1. 괄호열 선언 / cnt로 올바름 횟수 확인하기 (0으로 선언) / s로 받은 괄호열을 d(deque)로 가져오기
s = "[]{()}" 
cnt = 0
d = deque(s)

#2. 괄호열 길이만큼 for문을 돌려서 올바름 횟수 체크하기
for i in range(len(s)) :
    stack = [] #매 문자열 초기화
    is_valid = True #초기 선언
    pairs = {')': '(', ']': '[', '}': '{'}

    
    
    #2-1. d 문자열의 첫 번째 글자부터 마지막 글자까지 for문을 통해 확인하기
    for char in d:
        if char in "({[":
            # 여는 괄호는 스택에 저장
            stack.append(char)
        else:
            # 닫는 괄호인데 스택이 비었거나 짝이 안 맞으면 실패
            if not stack or stack.pop() != pairs[char]:
                is_valid = False
                break
    
    # 스택에 남은 게 없어야 최종 성공
    if is_valid and len(stack) == 0:
        cnt += 1
    
    # 다음 검사를 위해 왼쪽으로 1칸 회전
    d.rotate(-1)
    print(f"{i+1}회전 후 상태: {''.join(d)}, 올바른가?: {is_valid and len(stack) == 0}")

print(f"\n최종 결과: {cnt}")
