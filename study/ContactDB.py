import cx_Oracle



class ContactDB:

    def __init__(self, conn):
        self.con_name = conn
    
    def create_cls(self):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()

<<<<<<< HEAD
    def input_db(self, private_information):
=======
        items = [
                 (1,'친구')
                ,(2,'가족')
                ,(3,'회사')
                ,(4,'기타')
                ]
        sql = "INSERT INTO CLASSIFICATION VALUES (:1,:2)"
        
        for row in items:
            cursor.execute(sql,row)
        
        cursor.close()
        conn.commit()
        conn.close()
        
    def input_db(self,private_information):
>>>>>>> 3a9527fafea2906072f5761b73800fcce5613dc2
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()

        number = int(private_information['number'])
        classification = int(private_information['classification'])

<<<<<<< HEAD
        # cls_sql = "insert into classification values(:CLS_NUM,:CLS_NAME)"
        contact_sql = "insert into contact values(:1,:2,:3,:4,:5)"

        # if classification == 1:
        #     cls_name = '가족'
        # elif classification == 2:
        #     cls_name = '친구'
        # elif classification == 3:
        #     cls_name = '회사'
        # elif classification == 4:
        #     cls_name = '기타'

        # cls_data = (classification, cls_name)
        # print(cls_data)
        data = (
            private_information['name'],
            private_information['phone_number'],
            private_information['email'],
            classification,
            number
        )
        # cursor.execute(cls_sql, cls_data)
        cursor.execute(contact_sql, data)
        print(data)
        # print(cls_data)
=======
        contact_sql = "insert into contact values(:1,:2,:3,:4,:5)"

        data = (
                private_information['name'],
                private_information['phone_number'],
                private_information['email'],
                classification,
                number
                )

        cursor.execute(contact_sql, data)
>>>>>>> 3a9527fafea2906072f5761b73800fcce5613dc2

        cursor.close()
        conn.commit()
        conn.close()

    def select_db(self):
<<<<<<< HEAD

        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        sql = "select * from classification"
        cursor.execute(sql)

        for row in cursor:
            print(row)

        cursor.close()
        conn.close()

    def update_db(self):

        conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
        cursor = conn.cursor()
        sql = "DELETE FROM CONTACT WHERE "

        cursor.execute(sql)
        cursor.close()
        conn.commit()
=======
        
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        #sql = "select * from contact"
        sqls = "select * from classification"
        #cursor.execute(sql)
        cursor.execute(sqls)
        
        for row in cursor:
            print(row)
        
        cursor.close()
        conn.close()

    def update_db(self):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        sql = "DELETE FROM CONTACT WHRE "
        
        cursor.execute(sql)
        cursor.close()
        cursor.comit()
>>>>>>> 3a9527fafea2906072f5761b73800fcce5613dc2
        conn.close()
