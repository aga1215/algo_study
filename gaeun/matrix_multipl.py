'''
행렬의 곱셈: 2차원 행렬 arr1과 arr2를 입력받아, 
arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
'''

def solution(arr1, arr2):
    arr1_row = len(arr1) # 행렬 arr1의 행 개수
    arr2_col = len(arr2[0]) # 행렬 arr2의 열 개수
    K = len(arr2) # 행렬 arr2의 행 개수 = 행렬 arr1의 열 개수 = 곱셈 연산에 사용되는 공통 차원
    
    answer = [[0 for _ in range(arr2_col)] for _ in range(arr1_row)] 
    
    for i in range(arr1_row): 
        for j in range(arr2_col):
            for k in range(K):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer