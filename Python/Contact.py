def private_info(**kwargs):

    print(kwargs)

def public_info(**kwargs):
    
    print(kwargs)

num = 0
def contact_program(num):

    while num != 5:
        num = int(input("번호를 입력하세요."))
        if num == 1:

            name = str(input("이름을 입력하세요."))
            phone_num = str(input("전화번호를 입력하세요."))
            gubun = str(input("관계를 입력하세요"))
            
            private_info(name=name,phone_num=phone_num,gubun=gubun)


    return num

num = contact_program(num)
print(num)

