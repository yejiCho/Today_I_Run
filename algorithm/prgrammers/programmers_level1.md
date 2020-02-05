# [프로그래머스 - 문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918)

```python

# testcase 7 실패

def solution(s):
    answer = True
    ss = ['1','2','3','4','5','6','7','8','9','0']
    sss = []
    s = list(s)
    for i in s:
        if i not in ss:
            del i
        else:
            sss.append(i)
            
    # print(sss)
               
    if len(sss) == 4 or len(sss) == 6 :
        
        return answer
    
    else:
        
        return False
    
    
# .isdigit()
# 문자열이 숫자인지 아닌지를 True, False로 리턴해줌
# isalpha()
# 문자열이 문자인지 아닌지를 True, False로 리턴해줌


def solution(s):

    return s.isdigit() and (len(s) == 4 or len(s) == 6)


# try/except
# 파이썬으로 프로그래밍 중에 다양한 에러가 발생할 수 있다.
# 이 에러가 발생하는 예외상황은 유연하게 프로그래밍을 할 수 있는 도구가 되기도 한다.

# VlaueError, IndexError, ImportError

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
        except ValueError: 
            result = False
        else:
            result = True
            
    else:
        result = False
    return result

```

# [프로그래머스-문자열 정수로 바꾸기](https://programmers.co.kr/learn/courses/30/lessons/12925)


```python
#(+,-) int형으로 취급가능

def solution(s):
    answer = int(s)

    return answer

# 다른사람 풀이 1

def strToInt(str):
    result = 0

    int(str)
    return int(str)

# test
print(strToInt("-1234"))

# 다른사람 풀이 2
    # str[::-1]: 주어진 스트링을 거꾸로 만듦
    # enumerate :한 글자당 인덱스를 배정해서 각 자리의 10의 지수만큼 곱해서 더해줌
    # "-1234" str[::-1] -> "4321-"
    #  4 * (10 ** 0) + 3 * (10 ** 1) + 2 * (10 **2) + 1 * (10 ** 3)를 한 이후에 "-" 는 이 숫자를 마이너스로 만들어 버립니다.
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):

        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));

```
# [문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916)

```python

def solution(s):
    answer = True
    p_list = []
    y_list = []
    for i in s:
        if i == 'p':
            p_list.append(i)
        elif i == 'P':
            p_list.append(i)
        elif i == 'y':
            y_list.append(i)
        elif i == 'Y':
            y_list.append(i)
    if len(p_list) == len(y_list):
        return True
    else:
        return False
    # print(p_list)
    # print(y_list)

# 다른사람풀이

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )


```

# [프로그래머스 - 가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)


```python

def solution(s):
    answer = ''
    mok = len(s)/2
    mok = int(mok)
    if len(s) % 2 == 0:
        answer = s[mok-1:mok+1]
    else:
        answer = s[mok]
    return answer


# 다른사람 풀이

# /  : 나누기
# // : 몫
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]


print(string_middle("power"))
```

# [프로그래머스 - 문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)


```python

# 1차실패

def solution(strings, n):
    answer = []
    answers = []
    # for i,list_string in enumerate(strings):
    #     print(i,list_string)
    for i,list_string in enumerate(strings):
        answers.append(strings[i][n])
        answers.sort()
        if strings[i][n] == answers[n]:
            answer.append(list_string)
    print(answers)
    print(answer)
    return answer


```


# [프로그래머스 - 서울에서 김서방 찾기](https://programmers.co.kr/learn/courses/30/lessons/12919)

```python

def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = f'김서방은 {i}에 있다'
    return answer

```