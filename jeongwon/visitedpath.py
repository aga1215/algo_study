def solution(dirs):
    edges = set()
    x, y = 0, 0
    for i in dirs:
        # 이동 시키기
        if i == 'U': 
            nx = x
            ny = y + 1
        elif i == 'D':
            nx = x
            ny = y - 1
        elif i == 'L': 
            nx = x - 1
            ny = y
        elif i == 'R': 
            nx = x + 1
            ny = y
        # 조건 확인
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            edge = tuple(sorted([(x, y), (nx, ny)]))
            edges.add(edge)
        else: continue
        
        x = nx
        y = ny
    
    return len(edges)

s = input()
print(solution(s))
