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