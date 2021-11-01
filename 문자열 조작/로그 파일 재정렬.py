# 937
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
numbers = []
letters = []
for value in logs:
    if value.split()[1].isdigit():
        numbers.append(value)
    else:
        letters.append(value)

letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters + numbers)

# 틀렸음(v)
'''
1. 식별자를 제외한 두번째 문자가 숫자이면 입력된 순서대로 출력되고 문자이면 조건들에 의해 정렬한 후 출력이 이뤄줘야 한다
2. 숫자배열과 문자배열 두개로 나누어서 숫자와 문자를 구별해준다(문자열.split()[1] => 문자열을 공백을 기준으로 나눈 배열 생성후 1번 인덱스 해당값 선택)
3. 숫자배열은 그대로 출력된다고 했으니 그대로 두고 문자배열은 식별자를 제외한 문자들을 순서대로 비교해가며 오름차순으로 정렬해주고 만약 모든 문자가 같은
경우 마지막에는 식별자를 통해 정렬해준다(lambda 사용시에 그냥 x: (x[1:], x[0])이 아니다. 이렇게 해주면 letters 배열이 
['g1 act car', 'ab1 off key dog', 'a8 act zoo'] 일때 각각 1, b, 8을 대상으로 정렬하기 때문에 x.split()을 통해 단어로 나눈 다음 
x.split()[1:]이나 x.split()[0]을 이용해야 한다(x.split()[1:]인 이유는 두번째 단어로만 정렬하는 것이 아니라 모든 단어를 비교해야 하기 때문이다'''