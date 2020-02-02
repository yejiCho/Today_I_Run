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
public_info = {}
def contact_program(num):
    # list_private_info = []

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

            keys = list(public_info.keys())
            # print(keys)
            for i in keys:

                if rename == public_info[i]['name']:
                    # print(i[0])
                    print(str(keys.index(i)+1) +"."+ str(public_info[i]['name']+public_info[i]['phone_num']+public_info[i]['gubun']))


            renum = int(input("수정할 회원의 번호를 입력하세요"))

            for i in keys:
                if renum-1 == (keys.index(i)):

                    del public_info[i]

                    private_info = {}
                    name = str(input("이름을 입력하세요."))
                    phone_num = str(input("전화번호를 입력하세요."))
                    gubun = str(input("관계를 입력하세요"))

                    private_info['name'] = name
                    private_info['phone_num'] = phone_num
                    private_info['gubun'] = gubun

                    public_info[phone_num] = private_info

            print(public_info)

        elif num == 4:

            delname = str(input("삭제할 회원 이름을 적으세요."))

            keys = list(public_info.keys())
            # print(keys)
            for i in keys:

                if delname == public_info[i]['name']:
                    # print(i[0])
                    print(str(keys.index(i) + 1) + "." + str(
                        public_info[i]['name'] + public_info[i]['phone_num'] + public_info[i]['gubun']))
                else:
                    print("없는 이름입니다.")

            delnum = input("삭제할 번호를 적으세요.")

            for i in keys:
                if int(delnum)-1 == (keys.index(i)):

                    del public_info[i]


            print(public_info)
            print("삭제되었습니다.")


        elif num == 5:
            print("종료하겠습니다.")
            break




# return num

num = contact_program(num)
print(num)

