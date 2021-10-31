#5
s = "babad"

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

if len(s) < 2 or s == s[::-1]:
    print(s)

result = ''
for i in range(len(s) - 1):
    result = max(result,
                 expand(i, i + 1),
                 expand(i, i + 2),
                 key=len)

print(result)

#틀렸음
'''1. for문을 통해서 각각의 index에서 홀수 투포인터와 짝수 투포인터를 실행한 후 기존의 result, 홀수 투포인터 결과값, 짝수 투포인터
결과값을 비교한 후 가장 큰 값을 새로운 result 값으로 수정한다.(마지막 index는 홀수 및 짝수 투포인터를 적용할 수 없다...)
2. 각각의 투포인터 진행시 s[left] == s[right] 조건을 부합해야한다(처음에는 "왜 처음과 마지막만 비교하지... 중간 문자들이 서로 다를 수 
있잖아..."라고 생각했는데 처음부터 확장되서 진행이 되므로 현재 문자열을 대상으로 처음과 마지막 문자를 제외한 문자열은 팰린드롬 상태이다)'''