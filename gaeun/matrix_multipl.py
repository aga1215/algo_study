def solution(arr1, arr2):
    arr1_row = len(arr1) # arr1의 행의 개수
    arr2_col = len(arr2[0]) # arr2의 첫번째 줄 숫자의 개수
    N = len(arr2) # arr2의 행의 개수
    
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))] # 결과 행렬 초기화
    
    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(N):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer
        