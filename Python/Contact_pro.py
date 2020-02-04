import pickle


def main():

    prompt = """
    ===========================
    다음 메뉴 중 하나를 선택하세요.
    ============================
    1. 회원 추가
    2. 회원 목록 보기
    3. 회원 목록 수정하기
    4. 회원 삭제하기
    5. 종료하기

    """
    print(prompt)


def contact_program():

    print("등록할 회원의 정보를 입력하세요.")
    name = input("이름: ").strip()
    phone_number = input("전화번호 (ex: 01012345678):").strip()
    classification = input("구분 (ex: 가족, 친구,회사, 기타):").strip()

    classifications = ['가족','친구','회사','기타']
    # phone_numbers = ['0','1','2','3','4','5','6','7','8','9''\n']

    # for s in phone_number:
    #     if s not in phone_numbers:
    #         print("잘못된 전화번호 입력입니다.")

            # return {}

    if name == '':
        print("잘못된 이름입니다.")
        return {}

    for s in phone_number:
        if s not in str(range(10)):
            print("잘못된 전화번호 입력입니다.")

            return {}

    if phone_number == '':
        print("잘못된 전화번호 입력입니다.")

        return {}

    if classification not in classifications:
        print("잘못된 구분 입력입니다.")

        return {}

    if classification == '':
        print("잘못된 구분 입력입니다.")

        return {}


    private_information = { 'name' : name , 'phone_num' : phone_number , 'classification': classification}

    return private_information


def check_information(public_info):

    # phone_number , private_information = contact_program()
    input_name = input()

    keys = list(public_info.keys())
    list_input_name = []
    for key in keys:

        if input_name == public_info[key]['name']:
            list_input_name.append(input_name)

    print("총 %d 개의목록이 검색되었습니다." %len(list_input_name))

    for key in keys:

        if input_name == public_info[key]['name']:
            # print("총 %d 개의 목록이 검색되었습니다." % len(input_name))
            print(str(keys.index(key) + 1) + "." + "이름 = " +
                public_info[key]['name'] + "전화번호 : " + public_info[key]['phone_num'] +" 구분: " +public_info[key]['classification'])

    if input_name != public_info[key]['name']:

        print("해당하는 회원의 정보가 없습니다.")


def del_information(public_info):

    renum = input()

    keys = list(public_info.keys())

    for key in keys:

        if int(renum) - 1 == (keys.index(key)):

            del public_info[key]











