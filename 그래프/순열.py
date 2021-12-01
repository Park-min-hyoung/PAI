#46

# DFS를 활용한 순열 생성
def dfs(arr):
    if len(prev_arr) == len(nums):
        result.append(prev_arr[:])

    for value in arr:
        next_arr = arr[:]
        next_arr.remove(value)

        prev_arr.append(value)
        dfs(next_arr)
        prev_arr.pop()


nums = [1,2,3]
prev_arr = []
result = []

dfs(nums)
print(result)

# itertools 모듈 사용
'''from itertools import permutations

nums = [1,2,3]
print(list(map(list, permutations(nums))))'''

# 틀렸음
'''
1. 현재 주어진 노드 모음(리스트)에서 순서대로 방문, 방문한 노드를 제외한 노드들로 DFS를 해준다
2. 1번에서 방문한 노드를 제외한 노드 모음이 다음 순서에서는 현재 주어진 노드 모음이 된다'''