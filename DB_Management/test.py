import pyodbc
from init_Cursor import init_Cursor
from query import *

DBCONNECTOR=init_Cursor()
cursor=DBCONNECTOR.cursor
connection=DBCONNECTOR.connection

query_with_authorname(cursor,"Alice")
query_with_title(cursor,"Introduction")
query_with_tag(cursor,"C++")

rows = cursor.fetchall()

# 打印查询结果
for row in rows:
    print(row)
