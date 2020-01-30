
prompt = """

1. Add
2. List
3. Revise
4. Delete
5. Quit

Enter number :
"""
num = 0
# s_dic_list = []
# b_dic_list = []
dic = {}
b_dic_list = {}
while num != 4:
    print(prompt)
    num = int(input())
    if num == 1:
        name = ""
        
        phone_num = ""
        gubun   = ""
        name = str(input("이름을 입력하세요."))
        phone_num = str(input("전화번호을 입력하세요."))
        gubun   = str(input("구분을 입력하세요."))

        dic['name'] = name
        dic['phone_num'] = phone_num
        dic['gubun'] = gubun

        b_dic_list[phone_num] = dic
        # dic = {"이름": name, "전화번호":phone_num,"구분":gubun}
        # dic1 = {phone_num:dic}
        # s_dic_list.append(dic)
        # b_dic_list.append(dic1)


    elif num == 2:

        print("총 %d명의 회원이 저장되어있습니다."%len(b_dic_list))

        for i in range(len(b_dic_list)):
            print(b_dic_list)
            # list_b_dic = list(b_dic_list[i].values())
            # print(type(list_b_dic))
            # print(list_b_dic)


    # elif num == 3: