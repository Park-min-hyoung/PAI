#17

def dfs(index, path):
    if len(path) == len(digits):
        result.append(path)
        return

    # index부터 끝까지 작업을 완료해야한다(위에서 밑으로)
    for i in range(index, len(digits)):
        # index에 해당하는 키판 문자열을 순회하면서 처리
        for j in tel_num[digits[i]]:
            dfs(i + 1, path + j)


digits = "239"
tel_num = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
           '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
result = []

dfs(0, "")
print(result)


# 틀렸음
'''
1. digits의 각 자릿수에 해당하는 키판 배열(문자열)을 DFS를 통해 한개씩 처리한다.
2. 키판 배열에 문자열에서 문자 1개를 처리할때 다음 자릿수에 대해서 1번 작업을 반복한다.
3. 작업을 반복하다 path와 digits의 길이가 같으면 결과값에 넣어주고 return 한다'''