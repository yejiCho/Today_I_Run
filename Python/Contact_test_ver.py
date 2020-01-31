
def contact_program():
    list_public_info = []
    public_info = {}
    num = 0
    while num != 5:

        num = int(input("번호를 입력하세요."))
        if num == 1:
            private_info = {}
            name = str(input("이름을 입력하세요."))
            phone_num = str(input("전화번호를 입력하세요."))
            gubun = str(input("관계를 입력하세요"))

            private_info['name'] = name
            private_info['phone_num'] = phone_num
            private_info['gubun'] = gubun

            public_info[phone_num] = private_info
            list_public_info.append(public_info)

        elif num == 2:

            print("총 %d명의 회원이 저장되어 있습니다."%len(public_info))
            for i in public_info:
         
                print(public_info[i]['name']+public_info[i]['phone_num']+public_info[i]['gubun'])

        elif num == 3:

            rename = str(input("수정할 회원 이름을 적으세요"))
            
            for i in public_info:

                if rename == public_info[i]['name']:
                    rename_list = public_info[i]['name'] + public_info[i]['phone_num'] + public_info[i]['gubun']
                    print(rename_list)
    



print(contact_program)




