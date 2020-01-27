# [프로그래머스-괄호변환](https://programmers.co.kr/learn/courses/30/lessons/60058)

```python

# def is_right(string):
#     strlen = 0
#     for i in range(len(string)):
        
#         if p[i] == '(':  strlen += 1
#         elif p[i] == ')': strlen -= 1
        
#         if strlen == 0:
#             return True
#         return False

# def solution(p):
#     answer = ''

#     # strlenr = 0
    

def balanced(p):
    num = 0
    temp = []
    for idx, value in enumerate(p):
        if value == ")":
            num -=1
        if value == "(":
            num +=1
        if num == 0:
            return idx

def is_right(string):
    temp = []
    for i in string:
        if i == "(":
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    if len(temp) != 0:
        return False
    return True

def solution(p):
   
    if p == "" or is_right(p): return p
   
    u, v = p[:balanced(p)+1], p[balanced(p)+1:]
   
    if is_right(u):
        
        string = solution(v)
        
        return u + string
   
    else:
       
        t = "("
       
        t += solution(v)
       
        t += ")"
        
        u = list(u[1:-1])
       
        for i in range(len(u)):
            if u[i] == '(': 
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
        t += "".join(u)
       
        return t


```