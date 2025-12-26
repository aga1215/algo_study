def solution(arr1, arr2):
    row = len(arr1)          # 결과에 세로 줄 몇개? (결과 줄 개수)
    column = len(arr2[0])    # 한 줄에 가로 칸 몇개? (결과 칸 개수)
    middle = len(arr1[0])    # 한 칸 만들때 몇번 곱해서 더하냐
    answer = [[0] * column for _ in range(row)]
    
#     arr1에 arr2를 곱한 결과를 반환
#     1. 줄 단위로 반복
    for r in range(row):
#         2. 그 줄의 칸 단위로 반복(각 칸을 만든다)
        for c in range(column):
            total = 0
#             3. 한 칸의 값을 계산(같은 자리끼리 곱해서 전부 더한다)
            for m in range(middle):
                total += arr1[r][m] * arr2[m][c]
            answer[r][c] = (total)
            
    return answer