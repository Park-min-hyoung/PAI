#39

def dfs(arr):
    if sum(prev_v[:]) == target:
        result.append(prev_v[:])
        return

    for num in arr:
        sum_value = sum(prev_v[:])
        # 지금까지 방문한 곳의 합과 다음 방문할 곳의 의 합이 target보다 크면
        # 더 이상 다음 방문할 level의 node 들을 방문할 필요가 없다
        if sum_value + num > target:
            break

        # 조합을 출력해야 하므로 num(다음에 방문할 노드 값)이 방문한 값의 가장 최근 값보다 커야 한다
        if prev_v and prev_v[-1] > num:
            continue

        prev_v.append(num)
        sum_value += num

        if sum_value <= target:
            dfs(arr)
            prev_v.pop()


candidates = [2,7,6,3,5,1]
target = 9
sum_arr = 0
prev_v = []
result = []

dfs(sorted(candidates))
print(result)
