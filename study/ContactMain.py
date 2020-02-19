from Contact import ContactProgram
from Contact import main
from Contact import File
from ContactDB import ContactDB

Contact_name = "ora_user/1234@localhost:1521/xe"
FILE_PATH = "contact.pickle"
file = File(FILE_PATH)
file_contact = file.get_contact()

contact_db = ContactDB(Contact_name)
contact = ContactProgram()
contact.set_all_contact(file_contact)

contact_db.create_cls()

while True:
    main()
    main_num = input("번호를 입력하세요. ")
    if main_num == '1':
        private_info = contact.input_contact()
        contact_db.input_db(private_info)
        # pass
    elif main_num == '2':
        contact.member_list()
        contact_db.select_db()
    elif main_num == '3':
        contact.check_information("수정")
    elif main_num == '4':
        contact.check_information("삭제")
    elif main_num == '5':
        save_contact = contact.get_all_contact()
        file.update_contact(save_contact)
        break
    else:
        print("없는 번호입니다. 다시입력하세요.")
