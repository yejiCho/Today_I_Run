# 콜라츠 추측

```python
# 처음부터 n의값이 1일경우도 생각해줘야함
# n == 1 일경우는 for문을 돌지않으니깐 return 0해줘야함
def solution(n):
    answer = 0
    if n == 1: return 0
    for answer in range(500):
        if n % 2 == 0:
            n = n / 2
        else:
            n = n *3 + 1
        if n == 1:
            return answer + 1
    return -1

```

# 제곱수

```python
# ex) 121 이라는 수가 주어지는데 그 수가 어떤수의 제곱해서 나올 수 있는수 이면
# (어떤수 + 1)제곱한 값을 return 해줘야함
# 불가능할 경우 return -1
# ex) 121 = 11 * 11
# (11+1)**2 = 144 return 해주기
# ex) 3 -> 1.xxx
# return -1

import math
def solution(n):
    answer = 0
    result = math.sqrt(n)
    result = int(result)
    if result**2 == n:
        answer = (result+1)**2
        return answer
    else:
        return -1

```