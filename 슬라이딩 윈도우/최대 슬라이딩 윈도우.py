#239

from collections import deque
import sys

nums = [1]
k = 1

queue = deque([nums])
result = []
while len(queue) >= k:
    print(queue[0:])
    result.append(max(queue[0:k]))
    queue.popleft()

print(result)

# 틀렸음