'''
시간복잡도: O(n)
'''

from collections import deque
n, k = map(int, input().split())
queue = deque(range(1, n+1))
print('<', end = '')

while len(queue) > 1:
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')

print(queue.popleft(), end = '>')
