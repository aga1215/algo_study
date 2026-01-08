def solution(name, yearning, photo):
    namelst = set(name)
    cnt = {}
    for i in range(len(name)):
        cnt[name[i]] = yearning[i]
        
    ans = []
    for item in photo:
        score = 0
        for p in item:
            if p in namelst:
                score += cnt[p]
            else: pass
        ans.append(score)
    return ans

# def solution(name, yearning, photo):
#     score_map = dict(zip(name, yearning))
#     return [sum(score_map.get(p, 0) for p in item) for item in photo]
