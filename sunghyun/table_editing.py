def solution(n, k, cmd):
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    down[n - 1] = -1
    
    stack = []
    
    for c in cmd:
        op = c.split()
        
        if op[0] == 'U':
            for _ in range(int(op[1])):
                k = up[k]
                
        elif op[0] == 'D':
            for _ in range(int(op[1])):
                k = down[k]
                
        elif op[0] == 'C':
            stack.append(k)
            prev, nxt = up[k], down[k]
            
            if prev != -1:
                down[prev] = nxt
            if nxt != -1:
                up[nxt] = prev
                
            k = nxt if nxt != -1 else prev
            
        elif op[0] == 'Z':
            node = stack.pop()
            prev, nxt = up[node], down[node]
            
            if prev != -1:
                down[prev] = node
            if nxt != -1:
                up[nxt] = node

    answer = ['O'] * n
    for i in stack:
        answer[i] = 'X'
        
    return "".join(answer)
