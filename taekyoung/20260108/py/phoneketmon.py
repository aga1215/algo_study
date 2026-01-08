def solution(nums):
    len_num = len(nums)
    poks = {}
    
    for n in nums:
        poks[n] = 1
    
    len_poks = len(poks)
    
    answer = min(len_num / 2, len_poks)
    return answer