import cx_Oracle

conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
cursor = conn.cursor()
# sql = "INSERT INTO CLASSIFICATION VALUES (:1,:2)"
# data = (1, '핑구')
# #
# print(data)
# cursor.execute(sql,data)
# cursor.close()
# conn.commit()
# conn.close()