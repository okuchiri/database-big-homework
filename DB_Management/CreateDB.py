import pyodbc

from init_Cursor import init_Cursor

#连接数据库,获取游标
DBConnection=init_Cursor()
cursor = DBConnection.cursor
connection = DBConnection.connection



# #创建User表
# cursor.execute("CREATE TABLE [User] ("
#                "user_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "username  VARCHAR(50) UNIQUE, "
#                "email VARCHAR(50), "
#                "password VARCHAR(50), "
#                "permission INT"
#                ")")
# connection.commit()
# #添加测试数据
# cursor.execute("INSERT INTO [User] (username, email, password, permission) VALUES ('admin', 'admin@example.com', '123456', 1)")
# connection.commit()

# # 创建Tag表
# cursor.execute("CREATE TABLE Tag ("
#                "tag_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "name VARCHAR(50)"
#                ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO Tag (name) VALUES ('Python')")
# cursor.execute("INSERT INTO Tag (name) VALUES ('Java')")
# cursor.execute("INSERT INTO Tag (name) VALUES ('C++')")
# connection.commit()

# #创建Author表
# cursor.execute("CREATE TABLE Author ("
#                "Author_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "name VARCHAR(50), "
#                "email VARCHAR(50),"
#                "affiliation VARCHAR(50)"
#                ")")
# connection.commit()
#
# # # 添加测试数据
# cursor.execute("INSERT INTO Author (name, email, affiliation) VALUES ('Alice', 'alice@example.com', 'School of Computer Science and Engineering')")
# cursor.execute("INSERT INTO Author (name, email, affiliation) VALUES ('Bob', 'bob@example.com', 'School of Computer Science and Engineering')")
# connection.commit()

# #Journal表
# cursor.execute("CREATE TABLE Journal ("
#                "Journal_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "name VARCHAR(50)"
#                ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO Journal (name) VALUES ('Journal of Computer Science and Technology')")
# connection.commit()

# #Document表
# cursor.execute("CREATE TABLE Document ("
#                "document_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "title VARCHAR(50), "
#                "publication_date DATE, "
#                "src_url VARCHAR(50)"
#                "keywords VARCHAR(50)"
#                 ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO Document (title, publication_date, src_url) VALUES ('Introduction to Database Systems', '2021-01-01', 'https://www.db.cs.cmu.edu/db-book/')")
# connection.commit()


# #创建DocumentTag表
# cursor.execute("CREATE TABLE DocumentTag ("
#                "document_id INT, "
#                "tag_id INT, "
#                "PRIMARY KEY (document_id, tag_id), "
#                "FOREIGN KEY (document_id) REFERENCES Document(document_id), "
#                "FOREIGN KEY (tag_id) REFERENCES Tag(tag_id)"
#                ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO DocumentTag (document_id, tag_id) VALUES (1, 1)")
# cursor.execute("INSERT INTO DocumentTag (document_id, tag_id) VALUES (1, 2)")
# cursor.execute("INSERT INTO DocumentTag (document_id, tag_id) VALUES (1, 3)")
# connection.commit()

# #创建DocumentAuthor表
# cursor.execute("CREATE TABLE DocumentAuthor ("
#                "document_id INT, "
#                "author_id INT, "
#                "author_level INT default 1,"
#                "PRIMARY KEY (document_id, author_id), "
#                "FOREIGN KEY (document_id) REFERENCES Document(document_id), "
#                "FOREIGN KEY (author_id) REFERENCES Author(Author_id)"
#                ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO DocumentAuthor (document_id, author_id) VALUES (1, 1)")
# cursor.execute("INSERT INTO DocumentAuthor (document_id, author_id) VALUES (1, 2)")
# connection.commit()

# #创建JournalPos表
# cursor.execute("CREATE TABLE JournalPos ("
#                "document_id INT, "
#                "journal_id INT, "
#                "issue VARCHAR(50), "
#                "pages VARCHAR(50), "
#                "PRIMARY KEY (document_id, journal_id), "
#                "FOREIGN KEY (document_id) REFERENCES Document(document_id), "
#                "FOREIGN KEY (journal_id) REFERENCES Journal(Journal_id)"
#                ")")
# connection.commit()
#
# # 添加测试数据
# cursor.execute("INSERT INTO JournalPos (document_id, journal_id, issue, pages) VALUES (1, 1, '1', '1-10')")
# connection.commit()

# #创建Upload表
# cursor.execute("CREATE TABLE Upload ("
#                "document_id INT, "
#                "user_id INT,"
#                "primary key (document_id, user_id), "
#                "foreign key (document_id) references Document(document_id), "
#                "foreign key (user_id) references [User](user_id)"
#                ")")
# connection.commit()
#
# #测试数据
# cursor.execute("INSERT INTO Upload (document_id, user_id) VALUES (1, 1)")
# commit = connection.commit()


# 查询数据
# cursor.execute("SELECT * FROM DocumentAuthor")
# cursor.execute("SELECT * FROM [User]")
# cursor.execute("SELECT Document.title, Tag.name FROM Document , Tag,DocumentTag "
#                "where Document.document_id = DocumentTag.document_id and Tag.id = DocumentTag.tag_id")
# cursor.execute("SELECT Document.title, Author.name FROM Document,Author,DocumentAuthor "
#                 "where Document.document_id = DocumentAuthor.document_id and Author.Author_id = DocumentAuthor.author_id")
# cursor.execute("SELECT Document.title, Journal.name, JournalPos.issue, JournalPos.pages FROM Document,Journal,JournalPos "
#                 "where Document.document_id = JournalPos.document_id and Journal.Journal_id = JournalPos.journal_id")
#
# #添加docsrc表
# cursor.execute("CREATE TABLE docsrc ("
#                "Src_id INT IDENTITY(1,1) PRIMARY KEY, "
#                "document_id INT foreign key references Document(document_id),"
#                "src_url VARCHAR(50),"
#                "file_data VARBINARY(MAX)"
#                ")")
# connection.commit()
# #添加测试数据
# cursor.execute("INSERT INTO docsrc (document_id, src_url, file_data) VALUES (1, 'https://www.db.cs.cmu.edu/db-book/dbbook.pdf', null)")
# connection.commit()



# cursor.execute("SELECT Document.title, [User].username FROM Document,[User],Upload "
#                 "where Document.document_id = Upload.document_id and [User].user_id = Upload.user_id")
# rows = cursor.fetchall()
#
# # 打印查询结果
# for row in rows:
#     print(row)