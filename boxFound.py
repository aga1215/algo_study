# 4시 20분
# 5시 30분

def solution(n, w, num):
    stacks_dict = {}
    stack_names = [int(i) for i in range(1, w + 1)]

    #1) w 개수 만큼의 stack 생성
    for j in stack_names:
        stacks_dict[j] = []


    #2) 박스 넣기
    name = 1
    k = 1
    floor = True
    while int(k) <= n :
        if floor == True :
            stacks_dict[name].append(k)
            name +=1
            k +=1
        elif floor == False :
            stacks_dict[name].append(k)
            name -= 1
            k += 1

        if name > w: 
            floor = False
            name = w 
        elif name < 1:
            floor = True
            name = 1 


    #3) 값 꺼내기
    target = num
    found_name = None

    #3-1) 어느 스택에 있는지 먼저 찾기
    for name, stack in stacks_dict.items():
        if target in stack:
            found_name = name
            current_stack = stack
            break
    
    #3-2) 어느 스택에 있는지 찾았다면 몇 개를 꺼내야 하는지 세기
    if found_name:
        target_idx = current_stack.index(target)
        answer = len(current_stack) - target_idx


    
    return answer
