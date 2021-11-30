#3
import collections

s = "abcabcbb"
used = collections.defaultdict(int)
start = 1
max_len = 0

for idx, char in enumerate(s, 1):
    if used[char] and start <= used[char]:
        start = used[char] + 1
    else:
        max_len = max(max_len, idx - start + 1)

    used[char] = idx

print(max_len)

# 틀렸음
'''1. 해시를 이용해 현재 index의 문자를 방문했었는지 check 할 수 있다.
2. 현재 index의 문자가 해시에 있다면 진행중인 슬라이싱에 문자가 포함되어 있으므로 해쉬에 저장되어있는 index 값 + 1로 first를 초기화한다
(단 해시 저장되어 있는 index는 슬라이딩에 포함되어 있어야 하므로 first보다 크거나 같아야한다.(슬라이딩에 포함되어 있지 않으면 안된다))
3. 현대 index의 문자가 해시에 없다면 최대 길이와 새로운 문자가 포함된 문자열의 길이를 비교해 개수를 초기화 한다 
'''