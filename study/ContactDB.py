import cx_Oracle



class ContactDB:

    def __init__(self, conn):
        self.con_name = conn
    
    def create_cls(self):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()

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
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()

        number = int(private_information['number'])
        classification = int(private_information['classification'])

        contact_sql = "insert into contact values(:1,:2,:3,:4,:5)"

        data = (
                private_information['name'],
                private_information['phone_number'],
                private_information['email'],
                classification,
                number
                )

        cursor.execute(contact_sql, data)

        cursor.close()
        conn.commit()
        conn.close()

    def select_db(self):
        
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
        conn.close()
