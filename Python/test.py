# a = [1,2,3,4]
# result = [num*3 for num in a if num % 2 == 0]
# print(result)
# a ={}
# a['name'] = 1
# print(a)

# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)

# print(result)

# result = [x*y for x in range(2,10)
#     for y in range(1,10)]

# print(result)

# a = {'key':'value','key1':'value'}
# b = {'key':'value'}

a = {}
value   = 1
name    = 11
test    = 10
a['name','value'] = name, value
print(a)

b = {}

b['name'] = name
b['value'] = value
b['test'] = test
print(b)

# c = {}
c = {test:b}
bb = list(b.values())
# print(list(c.values()))
# print(c.keys())
print(c.values())
print(bb)

for i in range(len(bb)):
    print(bb[i])
# print(dict(c.values())
# print(type(c))

