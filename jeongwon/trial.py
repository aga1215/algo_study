def solution(answers):
    length = len(answers)
    first = [1, 2, 3, 4, 5] * (length//5 + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (length//8 + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length//10 + 1)
    cnt1, cnt2, cnt3 = 0, 0, 0

    # for a, b in zip(x, y) -> (a, b) 쌍으로 뽑을 수 있음
    for base, x, y, z in zip(answers, first, second, third):
        if base == x: cnt1 += 1
        if base == y: cnt2 += 1
        if base == z: cnt3 += 1
    
    cnt = [cnt1, cnt2, cnt3]
    # for i, c in enumerate(cnt) -> (0, 점수1), (1, 점수2), (2, 점수3) ...
    ans = [i+1 for i, c in enumerate(cnt) if c == max(cnt)]
    return ans

'''
def solution(answer):
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answer)):
        if answer[i] == (i % 5) + 1:
            cnt1 += 1

        if i % 2 == 0 and answer[i] == 2:
            cnt2 += 1
        elif i % 8 == 1 and answer[i] == 1:
            cnt2 += 1
        elif i % 8 == 3 and answer[i] == 3:
            cnt2 += 1
        elif i % 8 == 5 and answer[i] == 4:
            cnt2 += 1
        elif i % 8 == 7 and answer[i] == 5:
            cnt2 += 1
        
        if (i % 10 == 0 or i % 10 == 1) and answer[i] == 3:
            cnt3 += 1
        elif (i % 10 == 2 or i % 10 == 3) and answer[i] == 1:
            cnt3 += 1
        elif (i % 10 == 4 or i % 10 == 5) and answer[i] == 2:
            cnt3 += 1
        elif (i % 10 == 6 or i % 10 == 7) and answer[i] == 4:
            cnt3 += 1
        elif (i % 10 == 8 or i % 10 == 9) and answer[i] == 5:
            cnt3 += 1
        
    lst = [0, cnt1, cnt2, cnt3]
    maxvalue = max(cnt1, cnt2, cnt3)
    # print(lst)
    result = []
      
    for i in range(1, 4):
        if lst[i] == maxvalue:
            result.append(i)
            
    return result
'''
