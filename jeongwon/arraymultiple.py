def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    '''00 * 00 + 01 * 10 + 02 * 20
       00 * 01 + 01 * 11 + 02 * 21
       00 * 02 + 01 * 12 + 02 * 22
       
       10 * 00 + 11 * 10 + 12 * 20
       10 * 01 + 11 * 11 + 12 * 21
       10 * 02 + 11 * 12 + 12 * 22
       
       20 * 00 + 21 * 10 + 22 * 20
       20 * 01 + 21 * 11 + 22 * 21
       20 * 02 + 21 * 12 + 22 * 22
    '''
    for i in range(len(arr1)): # 행
        for j in range(len(arr2[0])): # 열
            for k in range(len(arr2)): # 제일 작은 단위 : 한 줄 안에서
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
