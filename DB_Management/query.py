import pyodbc
from init_Cursor import init_Cursor

#新建各种基本实体
def new_User(cursor,username,password,email=None,permission=1):
    sql="""
            INSERT INTO [User] (username,password,email,permission) 
        OUTPUT INSERTED.user_id 
        VALUES (?,?,?,?)
    """
    cursor.execute(sql, (username,password,email,permission))
    result = cursor.fetchone()  # 获取结果
    if result:
        user_id = result[0]
    else:
        raise Exception("插入失败，未返回 user_id")
    cursor.commit()  # 提交事务
    return user_id

def new_Author(cursor,authorname,email = None, affiliation = None):
    sql="""
            INSERT INTO Author (name,email,affiliation) 
        OUTPUT INSERTED.author_id 
        VALUES (?,?,?)
    """
    cursor.execute(sql, (authorname,email,affiliation))
    result = cursor.fetchone()  # 获取结果
    if result:
        author_id = result[0]
    else:
        raise Exception("插入失败，未返回 author_id")
    cursor.commit()  # 提交事务
    return author_id

def new_Tag(cursor,tagname):
    sql="""
            INSERT INTO Tag (name) 
        OUTPUT INSERTED.tag_id 
        VALUES (?)
    """
    cursor.execute(sql, tagname)
    result = cursor.fetchone()  # 获取结果
    if result:
        tag_id = result[0]
    else:
        raise Exception("插入失败，未返回 tag_id")
    cursor.commit()  # 提交事务
    return tag_id

def new_Journal(cursor,journalname):
    sql="""
            INSERT INTO Journal (name) 
        OUTPUT INSERTED.journal_id 
        VALUES (?)
    """
    cursor.execute(sql, journalname)
    result = cursor.fetchone()  # 获取结果
    if result:
        journal_id = result[0]
    else:
        raise Exception("插入失败，未返回 document_id")
    cursor.commit()  # 提交事务
    return journal_id
    cursor.commit()

def new_Document(cursor,title,publication_date,src_url,):
    sql = """
           INSERT INTO Document (title, publication_date, src_url)
           OUTPUT INSERTED.document_id
           VALUES (?, ?, ?)
       """
    # 执行插入操作并获取返回的 document_id
    cursor.execute(sql, (title, publication_date, src_url))
    # 获取刚插入的 document_id
    result = cursor.fetchone()  # 获取结果
    if result:  # 确保结果不为 None
        document_id = result[0]
    else:
        raise Exception("插入失败，未返回 document_id")
    cursor.commit()  # 提交事务
    return document_id

#新建各种实体之间的关系
def new_DocumentAuthor(cursor,document_id,author_id):
    sql="""
            INSERT INTO DocumentAuthor (document_id,author_id) 
        VALUES (?,?)
        """
    cursor.execute(sql, (document_id,author_id))
    cursor.commit()

def new_DocumentTag(cursor,document_id,tag_id):
    sql="""
            INSERT INTO DocumentTag (document_id,tag_id) 
        VALUES (?,?)
        """
    cursor.execute(sql, (document_id,tag_id))
    cursor.commit()

def new_JournalPos(cursor,document_id,journal_id,issue=None,page=None):
    sql="""
            INSERT INTO JournalPos (document_id,journal_id,issue,pages) 
        VALUES (?,?,?,?)
        """
    cursor.execute(sql, (document_id,journal_id,issue,page))
    cursor.commit()

def new_Upload(cursor,user_id,document_id):
    sql="""
            INSERT INTO Upload (user_id,document_id) 
        VALUES (?,?)
        """
    cursor.execute(sql, (user_id,document_id))
    cursor.commit()

######################################################
#上传文件01
def upload_file(cursor,title,src,publicatio_date,user_id,author_id,tag_id,journal_id,issue,page):
    #先插入document
    document_id = new_Document(cursor,title,publicatio_date,src)
    #先插入document_author关系
    new_DocumentAuthor(cursor,document_id,author_id)
    #再插入document_tag关系
    new_DocumentTag(cursor,document_id,tag_id)
    #再插入journal_pos关系
    new_JournalPos(cursor,document_id,journal_id,issue,page)
    #最后插入upload关系
    new_Upload(cursor,user_id,document_id)
    cursor.commit()
    return document_id

######################################################
#各种查询函数

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
def query_all_journals(cursor):
    cursor.execute("""
                Select * From Journal
                """)
def query_all_document(cursor):
    cursor.execute("""
                Select * From Document
                """)
def query_document_id(cursor,title):
    cursor.execute("""
                Select document_id From Document
                where title = ?
                """, (title,))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result
def query_author_id(cursor,authorname):#返回一个列表里面包含多个author_id，名字相同的作者可能有多个
    cursor.execute("""
                Select author_id From Author
                where name = ?
                """, (authorname,))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result
def query_tag_id(cursor,tagname): #返回一个tag_id
    cursor.execute("""
                Select tag_id From Tag
                where name = ?
                """, (tagname,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        return result[0]
def query_journal_id(cursor,journalname): #返回一个journal_id
    cursor.execute("""
                Select journal_id From Journal
                where name = ?
                """, (journalname,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        return result[0]
def query_user_id(cursor,username): #返回一个user_id
    cursor.execute("""
                Select user_id From [User]
                where username = ?
                """, (username,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        return result[0]

######################################################
#删除关系
def delete_DocumentAuthor(cursor,document_id,author_id):
    cursor.execute("""
                DELETE FROM DocumentAuthor WHERE document_id = ? AND author_id = ?
                """, (document_id,author_id))
    cursor.commit()

def delete_DocumentTag(cursor,document_id,tag_id):
    cursor.execute("""
                DELETE FROM DocumentTag WHERE document_id = ? AND tag_id = ?
                """, (document_id,tag_id))
    cursor.commit()

def delete_JournalPos(cursor,document_id,journal_id):
    cursor.execute("""
                DELETE FROM JournalPos WHERE document_id = ? AND journal_id = ?
                """, (document_id,journal_id))
    cursor.commit()

#删除实体
def delete_Author(cursor,Author_id):
    cursor.execute("""
                DELETE FROM Author WHERE author_id = ?
                """, (Author_id,))
    cursor.commit()

def delete_Tag(cursor,Tag_id):
    cursor.execute("""
                DELETE FROM Tag WHERE tag_id = ?
                """, (Tag_id,))
    cursor.commit()

def delete_Journal(cursor,Journal_id):
    cursor.execute("""
                DELETE FROM Journal WHERE journal_id = ?
                """, (Journal_id,))
    cursor.commit()

def delete_User(cursor, User_id):
        update_upload_sql = "DELETE FROM upload WHERE user_id = ?"
        cursor.execute(update_upload_sql, (User_id,))
        delete_user_sql = "DELETE FROM [User] WHERE user_id = ?"
        cursor.execute(delete_user_sql, (User_id,))
        cursor.commit()









