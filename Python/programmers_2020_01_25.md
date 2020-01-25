# [프로그래머스-올바른 괄호](https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3)

```python

# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '('문자로 열렸으면 반드시 짝지어서 ')'문자로 닫혀야 한다는 뜻입니다. 예를 들어

# - '()()','(())()'는 올바른 괄호입니다.
# - ')()(','(()('는 올바르지 않은 괄호입니다.

# 입출력 예
#     S         |      answer
#   '()()'      |       true
#   '(())()'    |       true
#   ')()('      |       false
#   '(()('      |       false

# for 문 사용해서 S에 "("가 존재하면 개수를 1씩 더해준다.
# ")"가 존재하면 개수를 1씩 빼준다.
# 개수가 마이너스 값이 나오면 false출력
# for문을 정상적으로 돌았는데 개수가 0이 아니면 false출력

def solution(s):
    answer = True
    # ss = {'(':')'}
    left = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        
        elif s[i] == ')':
            if left <= 0:
                return False
            else:
                left -= 1
    if left == 0:
        return True
    else:
        return False


```