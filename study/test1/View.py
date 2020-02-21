from DTO import DTO

dto = DTO()
# 메뉴
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
    menu_num = input("번호를 입력하세요.").strip()

    return menu_num

def insert_index():
    print("등록할 회원의 정보를 입력하세요.")
    # number = input("번호 : ")
    name = input("이름: ").strip()
    phone_number = input("전화번호(ex:01012345678): ").strip()
    email = input("이메일주소 : ").strip()
    classification = input("구분(ex: 1)가족 2)친구 3)회사 4)기타").strip()

    dto.name = name
    dto.phone_number = phone_number
    dto.email = email
    dto.classification = classification

    return dto.list_dto()

def select_index(select_rows):
    print(select_rows)


    


# def select_index():