# [124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899)

```python

def solution(n):
    answer = ''

    num_dict = {1:"1",2:"2",0:"4"}
    mok = 1
    na = 1
    
    while mok != 0:
        mok = n //3
        na = n % 3
        
        if na == 0 :
            mok -= 1
            
        n = mok
            
        answer = num_dict[na] + answer
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.8MB)
# 테스트 7 〉	통과 (0.05ms, 10.6MB)
# 테스트 8 〉	통과 (0.04ms, 10.6MB)
# 테스트 9 〉	통과 (0.04ms, 10.6MB)
# 테스트 10 〉	통과 (0.04ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.6MB)
# 테스트 14 〉	통과 (0.04ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.10ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.7MB)
```


# [programmers-오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888)

```python

# 배열(맵) 
# record를 순회하면서
# Enter, Leave인 경우 유저 아이디와 함께 정답에 출력될 메세지의 종류를 기록해둡니다. 이렇게 기록해 둔 것을 : event
# Enter, Change인 경우 연관 배열을 이용하여 각 유저 아이디를 키로, 닉네임 값으로 저장. 최종 닉네임을 유저 아이디 별로 유지
# events를 순회하면서 채팅방에 출력할 메세지를 생성할 때, 연관 배열에 저장된 아이디 별 최종 닉네임을 이용

def solution(record):
    answer = []
    logs= []
    Dict = dict()

    for i in range(len(record)):
        events = record[i].split(" ")
        if events[0] == "Enter":
            Dict[events[1]] = events[2]
            logs.append([events[1],"님이 들어왔습니다."])

        elif events[0] == "Leave":
            logs.append([events[1],"님이 나갔습니다."])
        elif events[0] == "Change":
            Dict[events[1]] = events[2]

    for log in logs:
        Diction = Dict[log[0]]
        answer.append(Diction+log[1])

    return answer



# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.8MB)
# 테스트 2 〉	통과 (0.05ms, 10.7MB)
# 테스트 3 〉	통과 (0.08ms, 10.7MB)
# 테스트 4 〉	통과 (0.07ms, 10.7MB)
# 테스트 5 〉	통과 (0.60ms, 11.1MB)
# 테스트 6 〉	통과 (0.68ms, 11.1MB)
# 테스트 7 〉	통과 (0.57ms, 11MB)
# 테스트 8 〉	통과 (0.92ms, 11MB)
# 테스트 9 〉	통과 (0.84ms, 11.1MB)
# 테스트 10 〉	통과 (0.73ms, 11.2MB)
# 테스트 11 〉	통과 (0.40ms, 11MB)
# 테스트 12 〉	통과 (0.38ms, 11MB)
# 테스트 13 〉	통과 (0.69ms, 11.1MB)
# 테스트 14 〉	통과 (0.82ms, 11.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.7MB)
# 테스트 16 〉	통과 (0.05ms, 10.7MB)
# 테스트 17 〉	통과 (0.11ms, 10.7MB)
# 테스트 18 〉	통과 (0.10ms, 10.8MB)
# 테스트 19 〉	통과 (0.78ms, 11.1MB)
# 테스트 20 〉	통과 (0.59ms, 11MB)
# 테스트 21 〉	통과 (0.59ms, 11.1MB)
# 테스트 22 〉	통과 (0.58ms, 11MB)
# 테스트 23 〉	통과 (0.79ms, 11.2MB)
# 테스트 24 〉	통과 (0.83ms, 11.1MB)
# 테스트 25 〉	통과 (113.59ms, 159MB)
# 테스트 26 〉	통과 (110.34ms, 164MB)
# 테스트 27 〉	통과 (119.61ms, 166MB)
# 테스트 28 〉	통과 (124.51ms, 170MB)
# 테스트 29 〉	통과 (113.61ms, 170MB)
# 테스트 30 〉	통과 (90.87ms, 150MB)
# 테스트 31 〉	통과 (96.60ms, 146MB)
# 테스트 32 〉	통과 (90.95ms, 147MB)
```

# [programmers-멀쩡한 사각형](https://programmers.co.kr/learn/courses/30/lessons/62048/solution_groups?language=python3)

```python

import math
def gcd(m,n):
    if m < n:
        m ,n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

def solution(w,h):

        return w * h -(w+h-gcd(w,h))

#       정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.03ms, 10.6MB)
# 테스트 5 〉	통과 (0.03ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.8MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.04ms, 10.7MB)
# 테스트 9 〉	통과 (0.03ms, 10.7MB)
# 테스트 10 〉	통과 (0.04ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.6MB)
# 테스트 12 〉	통과 (0.03ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.8MB)
# 테스트 14 〉	통과 (0.06ms, 10.7MB)
# 테스트 15 〉	통과 (0.04ms, 10.6MB)
# 테스트 16 〉	통과 (0.04ms, 10.7MB)
# 테스트 17 〉	통과 (0.04ms, 10.7MB)
# 테스트 18 〉	통과 (0.04ms, 10.7MB)  

import math
def solution(w,h):

    return w * h -(w+h-math.gcd(w,h))


# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.04ms, 10.8MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.7MB)
# 테스트 7 〉	통과 (0.04ms, 10.8MB)
# 테스트 8 〉	통과 (0.04ms, 10.7MB)
# 테스트 9 〉	통과 (0.04ms, 10.7MB)
# 테스트 10 〉	통과 (0.04ms, 10.8MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.6MB)
# 테스트 13 〉	통과 (0.07ms, 10.7MB)
# 테스트 14 〉	통과 (0.04ms, 10.7MB)
# 테스트 15 〉	통과 (0.04ms, 10.7MB)
# 테스트 16 〉	통과 (0.04ms, 10.7MB)
# 테스트 17 〉	통과 (0.04ms, 10.7MB)
# 테스트 18 〉	통과 (0.04ms, 10.7MB)

# 유클리드 호제법 
# 유클리드 알고리즘은 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘

# case 1
# def gcd(m,n):
# 	if m < n:
# 		m, n = n, m
# 	if n == 0:
# 		return m
#     if m % n == 0:
# 		return n
# 	else:
# 		return gcd(n, m%n)

# case 2
# def gcd(m,n):
#     while n != 0:
#        t = m%n
#        (m,n) = (n,t)
#     return abs(m)

# case 3
# def gcd(m,n):
#     while n! = 0:
# 	    if m < n:
# 		    m, n = n, m
# 	    if n == 0:
# 		    return m
# 	    if m % n == 0:
# 		    return n


# 사각형을 좌표로 생각해서 풀어봄!
# 대각선은 (0,0) , (8,12)를 지나고 직선의 식은 , y = 3/2 x
# x가 2의 배수, y가 3의 배수일 때 점을 지남
# x:(2,4,6,8) , y:(3,6,9,12)

```

# [프로그래머스 - 괄호변환](https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3)

```python



```

# 개별문제
# [프로그래머스 - n진수 게임](https://programmers.co.kr/learn/courses/30/lessons/17687)

> 튜브가 활동하는 코딩 동아리에서는 전통적으로 해오는 게임이 있다. 이 게임은 여러 사람이 둘글게 앉아서 숫자를 하나씩 차례대로 말하는 게임인데, 규칙은 다음과 같다.

1. 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두번째 사람은 1, ... 열번째 사람은 9를 말한다.
2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번쩨 사람은 둘째 자리인 0을 말한다.

> 이렇게 게임을 진행할 경우, 
>
>

##### 제한사항

##### 입출력 예

##### 입출력 예 설명


```python


# 반복문과 진법 변환 이용
# 챔퍼나운 수라는 수학상수 이용 <https://en.wikipedia.org/wiki/Champernowne_constant>


```