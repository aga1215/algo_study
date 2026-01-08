from collections import Counter
def solution(nums):
    cnt = Counter(nums)
    max = len(cnt)
    if len(nums)//2 < max:
        max = len(nums)//2
    return max
