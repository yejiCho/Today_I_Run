# from Contact import input_contact
import Contact

main_num = ''
public_info = {}

while True:
    Contact.main()
    main_num = input("번호를 입력하세요. ")

    if main_num == '1':
        private_info = Contact.input_contact()
        if private_info:
            public_info[private_info['phone_number']] = private_info
        else:
            print("정보가 없습니다.")
    elif main_num == '2':
        Contact.member_list(public_info)
    elif main_num == '3':
        Contact.check_information(public_info,"수정")
    elif main_num == '4':
        Contact.check_information(public_info,"삭제")

    elif main_num == '5':
        print("종료합니다.")
        break
    else:
        print("없는 번호입니다. 다시입력하세요.")
