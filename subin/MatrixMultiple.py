'''
두 행렬 A와 B를 곱하려면 첫 번째 행렬의 열 개수와 두 번째 행렬의 행 개수(N)가 같아야 합니다.
A가 (M x N) 크기라면, B는 반드시 (N x P) 크기여야 합니다.
결과 행렬의 크기는 (M x P)가 됩니다.
'''

def solution(arr1, arr2):
    #1) 두 행렬을 합친 결과행렬 만들기 : 결과값의 행과 열의 개수 만큼 크기 제작
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            row.append(0)
        answer.append(row)
   
    #2) 두 행렬의 곱한 값을 넣기
    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            num = 0
            for k in range(len(arr1[0])) :
                num = num + (arr1[i][k]*arr2[k][j])
            answer[i][j] = num
            
            
    return answer
