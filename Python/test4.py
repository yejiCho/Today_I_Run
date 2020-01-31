# def print_kwargs(**kwargs):
#     # print(kwargs)

#     return kwargs

# print(print_kwargs(a=1,b=2,c=2))

a = str(input("1. "))
b = str(input("2. "))
c = str(input("3. "))
    

def print_kwargs(**kwargs):
    
    return kwargs

print(print_kwargs(name=a,cl=b,tes=c))


f = open("contact.txt",'w')
name = str(input("이름을 입력하세요."))
phone_num = str(input("전화번호를 입력하세요."))
relation = str(input("관계를 입력하세요."))
private_info = {}
private_info = {'name':name,'phone_num':phone_num,'relation':relation}
public_info = {phone_num:private_info}
list_public_info = list(public_info)
list_public_information = "".join(list_public_info)
f.write(list_public_information)
f.close()
