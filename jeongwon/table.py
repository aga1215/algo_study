'''
8, 2-> 4 -> 4번 삭제 -> 1 -> 1번 삭제 -> 5 -> 5번 삭제 -> 3 -> 5번 복구 -> 1번 복구
trash stack, current stack
'''
# 정확성 통과 효율성 실패
def solution(n, k, cmd):
    trash = []  # 값, 삭제 당시 위치
    cur = [i for i in range(0, n)] 
    
    for item in cmd:
        if item.startswith('D'):
            x, cnt = map(str, item.split(' '))
            k += int(cnt)
        elif item.startswith('U'):
            x, cnt = map(str, item.split(' '))
            k -= int(cnt)
        elif item == 'C':
            temp = cur[k]
            trash.append((temp, k))
            cur.pop(k)
            
            if len(cur) == k:
                k -=1
        elif item == 'Z':
            temp, idx = trash[-1]
            cur.insert(idx, temp)
            trash.pop()
            if idx <= k: k += 1
            
    # print('final: ', cur, trash)
    
    ans = ['O'] * n
    for i in range(len(trash)):
        temp, idx = trash[i]
        ans[temp] = 'X'
    result = ''.join(map(str, ans))
    
    return result


# 테스트케이스만 성공 -> 채점 시 런타임 에러
def solution(n, k, cmd):
    trash = []
    cur = [i for i in range(0, n)]
    
    for item in cmd:
        if item.startswith('D'):
            cnt = item[-1]
            k += int(cnt)
        elif item.startswith('U'):
            cnt = item[-1]
            k -= int(cnt)
        elif item == 'C':
            cur.remove(k)
            trash.append(k)
        elif item == 'Z':
            temp = trash[-1] # 추가할 원소
            cur.append(temp) 
            trash.pop()
        print(cur, trash)
    
    print('final: ', cur, trash)
    ans = ['O'] * n
    
    for item in trash:
        ans[item] = 'X'
        # print(item)
    result = ''.join(map(str, ans))
    return result
  
