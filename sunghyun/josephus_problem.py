from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N + 1))
ans = []

while dq:
    dq.rotate(-(K - 1))
    ans.append(str(dq.popleft()))

print(f"<{', '.join(ans)}>")
