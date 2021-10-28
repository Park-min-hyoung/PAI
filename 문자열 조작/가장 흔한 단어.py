import operator

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 문자열에서 . 또는 , 제거한 문자열이 있는 리스트 생성
remove_paragraph = []
for ch in paragraph:
    if ch.isalpha() or ch == ' ':
        remove_paragraph.append(ch.lower())

# 각각의 문자 합쳐서 문자열 만든 다음에 공백을 기준으로 배열 생성
new_paragraph = list("".join(remove_paragraph).split())

# 사전을 통해 단어의 빈도수 정리
dict_paragraph = {}
for ch in new_paragraph:
    if dict_paragraph.get(ch) == None:
        dict_paragraph[ch] = 1
    else:
        value = dict_paragraph.get(ch)
        dict_paragraph[ch] = value + 1

result = sorted(dict_paragraph.items(), key=operator.itemgetter(1), reverse=True)

for i in range(len(result)):
    if banned == []:
        print(result[0][0])
        break
    if banned and result[i][0] not in banned:
        print(result[i][0])
        break


