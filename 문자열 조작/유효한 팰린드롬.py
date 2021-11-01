s = "A man, a plan, a canal: Panama"

# 정규표현식과 슬라이싱 이용
import re
s = s.lower()
s = re.sub('[^a-z0-9]', '', s)

print(s == s[::-1])

# Deque를 이용
'''strs = []
for target in s.lower():
    if target.isalnum():
        strs.append(target)

from collections import deque
queue_strs = deque(strs)
while len(queue_strs) > 1:
    if queue_strs.popleft() != queue_strs.pop():
        print(False)
        exit()

print(True)'''

# 내 풀이
'''strs = []
for target in s.lower():
    if target.isalnum():
        strs.append(target)

if strs == strs[::-1]:
    print('true')
else:
    print('false')'''