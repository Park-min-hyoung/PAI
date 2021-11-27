# 739

temperatures = [73,74,75,71,69,72,76,73]
stack = []
result = [0] * len(temperatures)

for i, temp in enumerate(temperatures):
    while stack and temp > temperatures[stack[-1]]:
        last = stack.pop()
        result[last] = i - last
    stack.append(i)

print(result)

# 틀렸음(v)
'''
1. 현재 온도를 기준으로 바로 전의 온도(stack[-1])가 낮을 경우 stack에서 이전 온도를 가져와서(stack.pop()) 현재 온도와의 차이를 result에 넣어준다.
그리고 현재 온도는 stack에 채워준다.'''