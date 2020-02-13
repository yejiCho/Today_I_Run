from Contact import ContactProgram
from Contact import main

contact = ContactProgram()

while True:
    main()
    main_num = input("번호를 입력하세요. ")
    if main_num == '1':
        private_info = contact.input_contact()
    elif main_num == '2':
        contact.member_list()
    elif main_num == '3':
        contact.check_information("수정")
    elif main_num == '4':
        contact.check_information("삭제")
    elif main_num == '5':
        print("프로그램 종료합니다.")
        break
    else:
        print("없는 번호입니다. 다시입력하세요.")