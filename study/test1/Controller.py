from View import main
from View import insert_index
from View import select_index
from DB import ContactDB

USERPATH = 'ora_user/1234@localhost:1521/xe'

contact_db = ContactDB(USERPATH)

while True:
    main_num = main()

    if main_num == '1':
        private_info = insert_index()
        contact_db.insert_db(private_info)
    elif main_num == '2':
        select_rows = contact_db.select_db()
        select_index(select_rows)
    # elif main_num == '3':
    
    # elif main_num == '4':
    
    elif main_num == '5':
        break
    else:
        print("없는 번호입니다. 다시 입력하세요.")