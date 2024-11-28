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


# res=login_query(cursor,"sdfga","123456")
# print(res)
# res=new_Document(cursor,"Introduction to JAVA","0001","None")
# print(res)
# res=new_Journal(cursor,"safsf")
# print(res)
# query_all_journals(cursor)
# query_all_document(cursor)
# res=new_Tag(cursor,"Qt")
# print(res)
# query_all_tags(cursor)

# res=new_Author(cursor,"seia")
# print(res)
# query_all_authors(cursor)
# res=new_User(cursor,"dfgfasdgf","123456")
# print(res)
# query_all_users(cursor)


# new_JournalPos(cursor,8,1)
# new_Upload(cursor,1,8)
# query_all_documents(cursor)
# rows = cursor.fetchall()
# new_Author(cursor,"seia")
# new_Author(cursor,"seia")
# new_Author(cursor,"seia")



# res=query_document_id(cursor,"Introduction to JAVA")
# print(res)
#
# upload_file(cursor,"abcasdads",None,"1-1-1",1,1,1,1,1,1)
# delete_DocumentAuthor(cursor,8,7)
# new_Upload(cursor,2,4)
# update_Author(cursor,5,"seia1","adadasdsdas@asdasd.asdasd","None")
# update_Tag(cursor,4,"QtCreator")
# update_Journal(cursor,5,"874498")
# update_User(cursor,4,"123465798641984","1234567890","None",1)
#update_Document(cursor,4,"Introduction to JavaAAAAAAAAAAAAAA","0001","None")

#new_filesrc(cursor,4,"https:://www.baidu.com/img/bd_logo1.png")
# file_data = "asfafsafsfsdfsdfsf".encode('utf-8')
# new_filedata(cursor,4,file_data)

# update_Document_src(cursor,1,"asfsfasfsfasfsdfas")
# delete_docsrc(cursor,4)

#update_User_permission(cursor,1,1000)

#new_DocumentAuthor(cursor,9,2,1)
#new_Document(cursor,"Introduction to PYT","0001","None","asjhdfgkjasgfkusf")

#new_DocumentAuthor(cursor,10,2,1)
new_DocumentTag(cursor,11,1)
query_all_journals(cursor)

# query_all_authors(cursor)
rows = cursor.fetchall()
# 打印查询结果
for row in rows:
    print(row)
