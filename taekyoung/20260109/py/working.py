def solution(schedules, timelogs, startday):
    answer = 0
    sun = 7 - startday
    sat = 6 if sun == 0 else 6 - startday
    
    for i in range(len(schedules)):
        maginot = schedules[i] + 10;
        if maginot % 100 >= 60:
            maginot += 40
        recieve = 1
        
        for t in range(7):
            if t != sun and t != sat:
                if timelogs[i][t] > maginot:
                    recieve = 0
        answer += recieve
        
    return answer