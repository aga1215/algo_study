from itertools import combinations
def solution(friends, gifts):
    cnt = [[0] * len(friends) for _ in range(len(friends))] # 개인별 주고 받은 선물
    lst = [[0] * 2 for _ in range(len(friends))] # 준 / 받은 선물 토탈 개수
    total = [0] * len(friends) # 다음달 받을 선물
    for item in gifts:
        give, receive = map(str, item.split(' '))
        giveidx, receiveidx = friends.index(give), friends.index(receive)
        cnt[giveidx][receiveidx] += 1
        
        lst[giveidx][0] += 1
        lst[receiveidx][1] -= 1
    
    score = [x + y for x, y in lst] # 선물 지수
    
    for targetidx, compare in combinations(range(len(friends)), 2):
        if targetidx == compare: pass
        else:
            if cnt[targetidx][compare] == cnt[compare][targetidx] or (cnt[targetidx][compare] == 0 and cnt[compare][targetidx] == 0):
                if score[targetidx] > score[compare]:
                    total[targetidx] += 1
                elif score[targetidx] < score[compare]:
                    total[compare] += 1
            elif cnt[targetidx][compare] > cnt[compare][targetidx]:
                total[targetidx] += 1
            elif cnt[targetidx][compare] < cnt[compare][targetidx]: 
                total[compare] += 1
    # print(total)

    return max(total)
