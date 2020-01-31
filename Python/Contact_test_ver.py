def contact_main():
    # prompt = ""
    prompt ='''
    =======================================
    다음 메뉴의 번호 중 하나를  선택하세요.
    =======================================
    1. 회원 추가
    2. 회원 목록 보기
    3. 회원 정보 수정하기
    4. 회원 삭제
    5. 종료
    '''
    # print (prompt)
    return prompt

def input_inforamtion():

    private_info = {}
    
    name = str(input("이름을 입력하세요."))
    phone_number = str(input("전화번호를 입력하세요."))
    relation = str(input("관계를 입력하세요."))

    private_info['name'] = name
    private_info['phone_num'] = phone_number
    private_info['relation'] = relation

    public_info[phone_number] = private_info
    list_public_info.append(public_info)
#   print(public_info)
#   print(list_public_info)
    
# print(contact_main())
list_public_info = []
public_info = {}
def contact_active():
    num = 0
    while num != 5:
        print(contact_main())
        num = int(input("숫자를 입력하세요"))    
        
        if num == 1:
            print(input_inforamtion())

        elif num == 2:

            print("총 %d명의 회원이 저장되어 있습니다."%len(public_info))
            for i in public_info:
                print(public_info[i]['name']+public_info[i]['phone_num'])

        elif num == 3:

            rename = str(input("수정할 회원 이름을 적으세요"))

            for i in public_info:
                if rename == public_info[i]['name']:
                    rename_list = public_info[i]['name'] + public_info[i]['phone_num']
                 #   print(type(rename_list))
                 

            

    return num
    
print(contact_active())
# print(private_info)
