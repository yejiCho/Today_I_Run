import cx_Oracle as cxo


class ContentError(Exception):
    def __str__(self):
        return "허용되지 않는 입력입니다."


def input_content(content):
    if content == "":
        raise ContentError()


def input_classification(classification,classifications):
    if classification not in classifications:
        raise ContentError()

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

class ContactProgram:
    def __init__(self):
        self.public_information = {}

    # def set_all_contact(self, contact):
    #     self.public_information = contact
    #
    # def get_all_contact(self):
    #     return self.public_information

    # 1번. 연락처 정보등록
    def input_contact(self):
        # conn = cxo.connect ("ora_user/1234@localhost:1521/xe")
        # cursor = conn.cursor()
        # sql = "insert into private values(:1,:2,:3)"
        print("등록할 회원의 정보를 입력하세요.")
        name = input("이름: ").strip()
        try:
            input_content(name)
        except ContentError as error_message:
            print(error_message)
            return {}
        phone_number = input("전화번호(ex:01012345678): ").strip()
        try:
            input_content(phone_number)
        except ContentError as error_message:
            print(error_message)
            return {}
        classification = input("구분(ex:가족,친구,회사,기타):").strip()
        classifications = ("가족","친구","회사","기타")

        try:
            input_classification(classification, classifications)
        except ContentError as error_message:
            print(error_message)
            return {}

        private_information = {
            'name':name,
            'phone_number':phone_number,
            'classification':classification
        }
        if private_information:
            self.public_information[private_information['phone_number']] = private_information
        else:
            print("정보가 없습니다.")
        data = (name, phone_number, classification)
        # cursor.execute(sql, data)
        # cursor.close()
        # conn.commit()
        # conn.close()
        return private_information


    # 2번. 연락처 목록조회
    def member_list(self):
        # conn = cxo.connect("system/1234@localhost:1521/xe")
        # cursor = conn.cursor()
        # sql = "select * from public"
        # cursor.execute(sql)

        for row in cursor:
            print(cursor)
        print(f"총 {len(self.public_information)}명의 회원이 저장되어 있습니다.")
        for phone_key in self.public_information.keys():
            # print(phone_key)
            print(f"이름={self.public_information[phone_key]['name']},"
                    f"전화번호={self.public_information[phone_key]['phone_number']},"
                    f"구분={self.public_information[phone_key]['classification']}")
        # cursor.close()
        # conn.close()

    # 3,4번. 수정,삭제
    def check_information(self,correct_comment):
        # conn = cxo.connect("system/1234@localhost:1521/xe")
        # cursor = conn.cursor()
        input_name = input(f"{correct_comment}이름을 입력하세요.")

        keys = list(self.public_information.keys())
        list_input_name = []
        for key in keys:
            if input_name == self.public_information[key]['name']:
                list_input_name.append(key)
        print(f'총{len(list_input_name)}개의 목록이 검색되었습니다.')
        # 이름이 같은 애들의 목록을 전체 조회해준다.
        for key in keys:
            if input_name == self.public_information[key]['name']:
                print(f"{str(keys.index(key)+1)}."
                    f"이름={self.public_information[key]['name']},"
                    f"전화번호={self.public_information[key]['phone_number']},"
                    f"구분={self.public_information[key]['classification']}")

        input_num = input(f"{correct_comment}할 번호를 입력하세요")
        del self.public_information[list_input_name[int(input_num)-1]]
        # sql = "delete from public where "
        # print(public_information)

        if correct_comment == "삭제":
            print(f"{correct_comment}가 완료되었습니다.")
        else:
            self.input_contact()
            print(f"{correct_comment}이 완료되었습니다.")