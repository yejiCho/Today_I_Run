import cx_Oracle

#  조회
# conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
# cursor = conn.cursor()
# sql = "select * from contact"
# cursor.execute(sql)
#
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.commit()
# conn.close()

# 추가
# conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
# cursor = conn.cursor()
# sql = "insert into CONTACT values (:1,:2,:3,:4,:5)"
# data = ('조예지', '01049505032', 1, 'goe152@naver.com',1)
#
# cursor.execute(sql, data)
# cursor.close()
# conn.commit()
# conn.close()

#  수정
conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
cursor = conn.cursor()
name = str(input("input name: "))
phone_num = str(input("input num: "))
classification = str(input("input classification: "))
sql = "update contact set name = " + name + "where phone_num" + phone_num
cursor.execute(sql)
cursor.close()
conn.commit()
conn.close()

#  삭제
# conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
# cursor = conn.cursor()
# sql = "delete from contact where cls_num = 1"
# cursor.execute(sql)
# cursor.close()
# conn.commit()
# conn.close()