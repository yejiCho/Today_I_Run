# def private_info(**kwargs):
#
#     return kwargs

# def main():

#     prompt = """
#     =============================
#     다음 메뉴 중 하나를 선택하세요.
#     =============================
#     1. 회원추가
#     2. 회원 목록 보기
#     3. 회원 목록 수정하기
#     4. 회원 삭제하기
#     5. 종료하기

#     Enter number :
#     """

num = 0
def contact_program(num):
    list_private_info = []
    list_public_info = []
    public_info = {}
    while num != 5:
        # main()

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
            # print(private_info)
        elif num == 2:
            # i = 1

            print("총 %d명의 회원이 저장되어 있습니다."%len(public_info))
            for i in public_info:
                # i = i+1
                # print(i)
                print(public_info[i]['name']+public_info[i]['phone_num']+public_info[i]['gubun'])

            # ("수정할 회원의 번호를 입력해주세요.")
                # print(list_public_info[i])

        elif num == 3:

            rename = str(input("수정할 회원 이름을 적으세요"))
            for i in public_info:
                # n = 0
                # for n in range(len(public_info)):
                if rename == public_info[i]['name']:
                    rename_list = public_info[i]['name'] + public_info[i]['phone_num'] + public_info[i]['gubun']
                    print(rename_list)

            # for n in range(len()):

            # for n in range(len(public_info)):
            #     print(public_info)
            #     print(str(n+1)+rename_list)

            re_num = int(input("수정할 회원의 번호를 입력하세요"))

            private_info = {}
            name = str(input("이름을 입력하세요."))
            phone_num = str(input("전화번호를 입력하세요."))
            gubun = str(input("관계를 입력하세요"))

            private_info['name'] = name
            private_info['phone_num'] = phone_num
            private_info['gubun'] = gubun

            public_info[phone_num] = private_info


        elif num == 4:

            delname = str(input("삭제할 회원 이름을 적으세요."))

        elif num == 5:
            print("종료하겠습니다.")
            break




# return num

num = contact_program(num)
print(num)

