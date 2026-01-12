def solution(arr):
    if not arr: return []
    
    answer = [arr[0]]
    
    # 1번 인덱스부터 마지막 인덱스까지 숫자로 순회
    for i in range(1, len(arr)):
        # 현재 값(arr[i])과 바로 이전 값(arr[i-1])을 비교
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer
