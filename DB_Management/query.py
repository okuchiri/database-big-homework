import pyodbc
from init_Cursor import init_Cursor

def new_User(cursor,username,password,email=None,permission=1):
    cursor.execute("""
                INSERT INTO [User] (username,password,email,permission) VALUES (?,?,?,?)
                """, (username,password,email,permission))
    cursor.commit()

#根据用户名跟密码查询用户是否存在，返回布尔值和用户id
def login_query(cursor,username,password):
    cursor.execute("""
                SELECT password,user_id FROM [User] WHERE username =?
                """, (username))
    result = cursor.fetchone()
    if result is None:
        return (False,None)
    else:
        bool_result = result[0] == password
        userid= result[1]
        return (bool_result,userid)

def query_all_users(cursor):
    cursor.execute("""
                SELECT * FROM [User]
                """)

def query_with_authorname(cursor,authorname):
    cursor.execute("""
                SELECT Document.title, Author.name 
                FROM Document, DocumentAuthor, Author 
                WHERE Author.name LIKE ? AND 
                      Document.document_id = DocumentAuthor.document_id AND 
                      DocumentAuthor.author_id = Author.author_id
            """, (f'%{authorname}%',))

def query_with_title(cursor,title):
    cursor.execute("""
                SELECT Document.title, Document.src_url FROM Document
                where Document.title like ?
                """, (f'%{title}%',))

def query_with_tag(cursor,tag):
    cursor.execute("""
                SELECT Document.title, Document.src_url FROM Document, DocumentTag, Tag
                where Document.document_id = DocumentTag.document_id and DocumentTag.tag_id = Tag.tag_id and Tag.name like ?
                """, (f'%{tag}%',))

def new_Author(cursor,authorname,email = None, affiliation = None):
    cursor.execute("""
                INSERT INTO Author (name,email,affiliation) VALUES (?,?,?)
                """, (authorname,email,affiliation))
    cursor.commit()

def query_all_authors(cursor):
    cursor.execute("""
                SELECT * FROM Author
                """)

def query_all_documents(cursor):
    cursor.execute("""
                Select * From Document
                """)

def query_all_tags(cursor):
    cursor.execute("""
                Select * From Tag
                """)

def new_Tag(cursor,tagname):
    cursor.execute("""
                INSERT INTO Tag (name) VALUES (?)
                """, (tagname,))
    cursor.commit()

def new_Journal(cursor,journalname):
    cursor.execute("""
                INSERT INTO Journal (name) VALUES (?)
                """, (journalname,))
    cursor.commit()

def query_all_journals(cursor):
    cursor.execute("""
                Select * From Journal
                """)

def new_Document(cursor,title,publication_date,src_url,):
    cursor.execute("""
                INSERT INTO Document (title,publication_date,src_url) VALUES (?,?,?)
                """, (title,publication_date,src_url))
    cursor.commit()

