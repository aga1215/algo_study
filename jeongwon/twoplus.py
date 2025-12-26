from itertools import permutations
def solution(numbers):
    ans = []
    for p in permutations(numbers, 2):
        temp = p[0] + p[1]
        if temp not in ans:
            ans.append(temp)
        else: 
            continue
    ans.sort()
    return ans
