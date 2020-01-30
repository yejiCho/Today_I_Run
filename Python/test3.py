# ex1)
def any_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = any_many(1,2,3)

print(result)

# ex2)
def print_kwargs(**kwargs):
    # print(kwargs)

    return kwargs

print(print_kwargs(a=1,b=2,c=2))

#  ex3)
def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(2,3))

# ex4) 함수 안에서 선언한 변수의 효력 범위_164
a = 1
def vartest(a):
    a = a + 1
    return a
# vartest(a)
print(vartest(a))
print(a)

# ex5) 
a = 1
def vartest1(a):
    a = a+1
    return a

a = vartest(a)
print(a)


# ex6)
a = 1
def vartest2():
    global  a
    a  = a+1

vartest2()
print(a)