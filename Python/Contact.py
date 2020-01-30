def private_info(**kwargs):

    # print(kwargs)
    return kwargs

print(num)

num = contact_program(num)
def contact_program(num):

    while num != 5:
        num = int(input("번호를 입력하세요."))
        if num == 1:

            name = str(input("이름을 입력하세요."))
            phone_num = str(input("전화번호를 입력하세요."))
            gubun = str(input("관계를 입력하세요"))
            print(private_info(name=name,phone_num=phone_num,gubun=gubun))
            # private_info('이름'=name,'전화번호'=phone_num, "구분"=gubun)
            # prin
        elif num == 2:



    # return num
# print( num = int(input("번호를 입력하세요")))
# print(num)