def solution(s):
    lst = []
    for i in s:
        if i == '(':
            lst.append(i)
        else: 
            if lst: # 비어있지 않으면
                lst.pop()
            else: # 비어있으면
                return False

    if not lst: # 비어있으면
        return True
    else: return False

s = input()
if solution(s):
  print('True')
else: print('False')
