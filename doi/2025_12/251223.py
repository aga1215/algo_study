def solution(numbers):
    answer = []
#     numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑기
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
#             두 개의 수를 더해 answer 배열에 없는 값이라면 저장
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
                # print(numbers[i]+numbers[j])
#     answer를 오름차순으로 정렬
    answer.sort()
    print(answer)
    return answer