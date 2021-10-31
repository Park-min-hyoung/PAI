
# 819
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
         if word not in banned]

count = collections.Counter(words)
print(count.most_common(1)[0][0])

# 틀렸음
'''1. 정규표현식 사용 및 하나의 리스트에 여러 메소드와 조건문 사용으로 입력값에 대한 전처리 작업
2. collections 모듈의 Counter 클래스를 이용해 가장 많이 등장하는 단어를 출력할 수 있다'''