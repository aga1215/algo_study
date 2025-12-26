def solution(numbers):
    #2) 두 숫자 합치기
    answer = set() #숫자를 합친 배열 / set을 사용해서 중복 제거 




    for i in range(len(numbers)) : #두 숫자 합치기 / / if 활용 범위 필터링
        for j in range(i+1, len(numbers)) : #i 이후의 요소들만 선택
            total = numbers[i] + numbers[j]
            answer.add(total)

    return sorted(list(answer))
