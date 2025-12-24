def solution(arr1, arr2):
    arr1_row = len(arr1) # arr1 행의 개수
    arr2_col = len(arr2[0]) # arr2 열의 개수
    K = len(arr2) # arr2 행의 개수
    
    answer = [[0 for _ in range(arr2_col)] for _ in range(arr1_row)]
    
    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(K):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
        