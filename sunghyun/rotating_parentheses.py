def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        rotated_s = s[i:] + s[:i]

        stack = []
        is_Valid = True

        for char in rotated_s:
            if char in "{[(":
                stack.append(char)
            else:
                if not stack:
                    is_Valid = False
                    break
            
                top = stack.pop()

                if char == "]" and top != "[":
                    is_Valid = False
                    break
                elif char == "}" and top != "{":
                    is_Valid = False
                    break
                elif char == ")" and top != "(":
                    is_Valid = False
                    break
        
        if is_Valid and not stack:
            answer += 1

    return answer
