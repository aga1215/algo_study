def solution(dirs):
    
    paths = set()
    cur_x, cur_y = 0, 0
    
    move_types = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    for move in dirs:
        # 1. 이동할 좌표(nx, ny) 계산
        if move == 'U':
            nx, ny = cur_x, cur_y + 1
        elif move == 'D':
            nx, ny = cur_x, cur_y - 1
        elif move == 'R':
            nx, ny = cur_x + 1, cur_y
        elif move == 'L':
            nx, ny = cur_x - 1, cur_y
        '''
        #if를 사용하지 않는 다른 방법으로는
        dx, dy = move_types[move]
        nx, ny = cur_x + dx, cur_y + dy
        '''

        # 2. 범위를 벗어나는지 확인 (벗어나면 continue)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 3. (현재좌표, 다음좌표)를 정렬해서 하나의 튜플로 만듦
            path = tuple(sorted([(cur_x, cur_y), (nx, ny)]))

            #4. 지나간 길 저장
            paths.add(path)

            # 5. 현재 위치 업데이트:
            cur_x, cur_y = nx, ny
    
    
    
    
    
    answer = len(paths)

    
    return answer
