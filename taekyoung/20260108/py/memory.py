def solution(name, yearning, photo):
    
    answer = []
    misses = {}
    for i in range(len(name)):
        misses[name[i]] = yearning[i]
    
    for v in photo:
        s = 0
        for p in v:
            s += misses.get(p, 0)
        answer.append(s)
    
    return answer