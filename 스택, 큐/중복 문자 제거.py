#316

# 스택을 이용한 문자 제거
'''s = "bcabc"
counter, stack, seen = Counter(s), [], set()

for i, ch in enumerate(s):
    counter[ch] -= 1
    if ch in seen:
        continue

    while stack and stack[-1] > ch and counter[stack[-1]] > 0:
        seen.remove(stack.pop())

    stack.append(ch)
    seen.add(ch)

return ''.join(stack)'''

# 재귀를 이용한 분리
'''def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''

print(removeDuplicateLetters(strs))'''

# 틀렸음
'''
재귀를 이용한 분리(x)
1. set를 이용해 중복문자를 제거 및 정렬 후 접미사 배열을 만들어 원래 배열과 함께 set을 사용해 같은지를 체크 한다.
2. 다르다면 접미사 쪽에서 어떠한 문자를 처리할 수 없는 경우로 만족하지 못하므로 해당 함수의 다음 반복문을 수행하고
같다고 하면 해당 문자를 return 하는 동시에 해당 문자가 제거된(replace()) suffix를 다음 함수의 문자열로 넘겨준다.
3. 1~2번의 과정을 반복하고 더 이상 suffix가 없을 때 백트래킹 되면서 결과가 조합된다
스택을 이용한 문자 제거(v)
1. Counter 클래스를 사용해 현재 문자를 기준으로 뒤쪽에 스택 top에 위치한 문자가 있는지 check 할 수 있으며, set을 통해
현재 문자가 set 있으면 다음 반복문으로 갈 수 있게끔 해 중복을 피할 수 있다.
2. 현재 문자가 최근 스택의 top의 문자보다 사전순으로 빠르고 아직 반복되지 않은 문자열 원소 중에(현재 문자 뒤쪽)
있다면 스택과 set에서 그 문자를 빼낸다.'''