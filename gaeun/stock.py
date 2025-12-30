def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        seconds = 0
        for j in range(i+1, n):
            seconds += 1
            if prices[i] > prices[j]:
                break
        answer.append(seconds)
    return answer