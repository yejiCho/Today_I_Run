import cx_Oracle

# class UserPath:
    # conn = cx_Oracle.connect()

class ContactDB:
    def __init__(self,conn):
        self.con_name = conn
    def insert_db(self,private_info):
        x = 0
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        cls_sql = "insert into classification values(:1,:2)"
        contact_sql = "insert into contact values(:1,:2,:3,:4,:5)"
        # print(private_info)
        # print(private_info[0])
        if private_info[4] == '친구':
            x = 1
        elif private_info[4] == '가족':
            x = 2
        elif private_info[4] == '회사':
            x = 3
        elif private_info[4] == '기타':
            x = 4
        cls_data = [
            x
            ,private_info[4]
        ]
        print(cls_data)
            
        data = (
            private_info[0]
            ,private_info[1]
            ,private_info[2]
            ,private_info[3]
            ,x
        )
        # print(data)
        # 0, 조, 010, goe, 구분
        cursor.execute(cls_sql,cls_data)
        cursor.execute(contact_sql,data)
        cursor.close()
        conn.commit()
        conn.close()
        # print(private_info)
    
    def select_db(self):

        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        sql = "SELECT * FROM contact"
        cursor.execute(sql)
        rows = []
        for row in cursor:
            # print(row)
            rows.append(row)
        # print(rows)
        cursor.close()
        conn.close()
        return rows