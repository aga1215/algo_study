def solution(participant, completion):
    user_data = {}

    # 1. 참가자 명단을 보며 인원수 증가 (+1)
    for name in participant:
        if name in user_data:
            user_data[name] += 1
        else:
            user_data[name] = 1

    # 2. 완주자 명단을 보며 인원수 감소 (-1)
    for name in completion:
        user_data[name] -= 1

    # 3. 남은 인원이 0보다 큰 사람이 완주하지 못한 동명이인!
    for name, count in user_data.items():
        if count > 0:
            return name
