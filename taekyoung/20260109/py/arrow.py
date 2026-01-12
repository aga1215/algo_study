best_score = 0
best = [0 for _ in range(11)]

def solution(n, info):
    global best, best_score
    answer = []
    
    for i in range(len(info)):
        if info[i] > 0:
            best_score -= 10 - i

    print(best_score)
            
    make_score(n, 0, best_score, info, [0 for _ in range(11)])
    print(best)

    if best_score <= 0:
        return [-1]
        
    return best

def make_score(n, k, cur_score, info, arrow):
    global best, best_score
    if n == 0 or k == 10:
        arrow[k] = n

        if cur_score > best_score:
            best_score = cur_score
            best = arrow
            return
        elif best_score > cur_score:
            return
        else:
            for i in range(10, -1, -1):
                if arrow[i] > best[i]:
                    best_score = cur_score
                    best = arrow
                    return
                elif best[i] > arrow[i]:
                    return
            return
    else:
        if n > info[k]:
            new_n = n - (info[k] + 1)
            new_arr = arrow[:]
            new_arr[k] = info[k] + 1
            new_score = 0
            if info[k] > 0:
                new_score = cur_score + (10 - k) * 2
            else:
                new_score = cur_score + 10 - k
            
            make_score(new_n, k + 1, new_score, info, new_arr)
        make_score(n, k + 1, cur_score, info, arrow)