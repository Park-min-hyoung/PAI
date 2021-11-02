#49
strs = ["eat","tea","tan","ate","nat","bat"]

# defaultdict를 이용한 방법
import collections

anagrams = collections.defaultdict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)

print(list(anagrams.values()))

# 내 방법
'''sort_strs = []

for i, word in enumerate(strs):
    sort_strs.append(''.join(sorted(word)))

set_strs = set(sort_strs)
result = []
for target in set_strs:
    array = []
    for idx, value in enumerate(sort_strs):
        if target == value:
            array.append(strs[idx])
    result.append(array)

print(result)'''