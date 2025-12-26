def solution(N, stages):
    ans = [-1]*(N+1)
    total = len(stages) # 사람 수
    for round in range(1, N+1):
        fail = stages.count(round)
        if fail == 0: # 모두 통과한 경우
            ans[round] = 0
        else:
            ans[round] = fail/total
            total -= fail
    # lambda: ans[i]를 기준으로 i를 정렬
    result = sorted(range(1, N+1), key=lambda i : ans[i], reverse=True)
    return result[:N]
 
