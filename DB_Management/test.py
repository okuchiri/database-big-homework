import pyodbc
from init_Cursor import init_Cursor
from query import *

DBCONNECTOR=init_Cursor()
cursor=DBCONNECTOR.cursor
connection=DBCONNECTOR.connection

# query_with_authorname(cursor,"Alice")
# query_with_title(cursor,"Introduction")
# query_with_tag(cursor,"C++")

#new_Author(cursor,"Bob")
#new_Journal(cursor,"safsa")
#query_all_journals(cursor)
#query_all_documents(cursor)
# new_User(cursor,"aasd","123456")
# new_User(cursor,"bob","123456")


res=login_query(cursor,"sdfga","123456")
print(res)

query_all_users(cursor)
rows = cursor.fetchall()

# 打印查询结果
for row in rows:
    print(row)
