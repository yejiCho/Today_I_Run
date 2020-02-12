def solution(s):
    
    answer = "".join(sorted(list(s),reverse = True))
    
    return answer

print(solution('Zbcdefg'))
print(solution('ZdksnFdkAfj'))
print(solution('AacBDdBCeWdD'))