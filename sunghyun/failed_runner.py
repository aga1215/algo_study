from collections import Counter

def solution(participant, completion):

    # 1. 참가자 이름별로 개수 세기 (예: "leo": 1, "kiki": 2...)

    part_counter = Counter(participant)

    # 2. 완주자 이름별로 개수 세기

    comp_counter = Counter(completion)

    # 3. 빼기 (남은 1명이 범인)

    answer = part_counter - comp_counter

    # 4. 키 값(이름)만 꺼내서 리턴

    return list(answer.keys())[0]
