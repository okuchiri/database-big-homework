import pyodbc


# 新建各种基本实体
def new_User(cursor, username, password, email="", permission=1):
    sql = """
            INSERT INTO [User] (username,password,email,permission) 
        OUTPUT INSERTED.user_id 
        VALUES (?,?,?,?)
    """
    try:
        cursor.execute(sql, (username, password, email, permission))
        result = cursor.fetchone()  # 获取结果

        if result:
            user_id = result[0]
            cursor.commit()
            return (True, user_id)  # 注册成功，返回成功标志和 user_id
        else:
            return (False, None)  # 插入失败，返回失败标志和 None
    except Exception as e:
        print(f"Error: {e}")
        return (False, None)

def new_Author(cursor, authorname, email = "", affiliation=None):
    sql = """
            INSERT INTO Author (name,email,affiliation) 
        OUTPUT INSERTED.author_id 
        VALUES (?,?,?)
    """
    cursor.execute(sql, (authorname, email, affiliation))
    result = cursor.fetchone()  # 获取结果
    if result:
        author_id = result[0]
    else:
        raise Exception("插入失败，未返回 author_id")
    cursor.commit()  # 提交事务
    return int(author_id)


def new_Tag(cursor, tagname):
    sql = """
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
    return int(tag_id)


def new_Journal(cursor, journalname):
    sql = """
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
    return int(journal_id)
    cursor.commit()


def new_Document(cursor, title, publication_date, src_url ,keywords=None):
    sql = """
           INSERT INTO Document (title, publication_date, src_url,keywords)
           OUTPUT INSERTED.document_id
           VALUES (?, ?, ?,?)
       """
    # 执行插入操作并获取返回的 document_id
    cursor.execute(sql, (title, publication_date, src_url,keywords))
    # 获取刚插入的 document_id
    result = cursor.fetchone()  # 获取结果
    if result:  # 确保结果不为 None
        document_id = int(result[0])
    else:
        raise Exception("插入失败，未返回 document_id")
    cursor.commit()  # 提交事务
    return document_id


# 新建各种实体之间的关系
def new_DocumentAuthor(cursor, document_id, author_id,author_level):
    # sql = """
    #         INSERT INTO DocumentAuthor (document_id,author_id,author_level)
    #     VALUES (?,?,?)
    #     """
    # cursor.execute(sql, (document_id, author_id,author_level))
    # cursor.commit()
    try:
        # 定义 SQL 插入语句
        sql = """
                INSERT INTO DocumentAuthor (document_id, author_id, author_level) 
                VALUES (?, ?, ?)
            """
        # 确保传递的参数是元组类型
        params = (document_id, author_id, author_level)
        # 执行 SQL 语句并传入参数
        cursor.execute(sql, params)
        # 提交事务
        cursor.connection.commit()
        return True

    except Exception as e:
        # 如果出现错误，回滚事务
        cursor.connection.rollback()
        print("An error occurred:", e)
        return False


def new_DocumentTag(cursor, document_id, tag_id):
    try:
        sql = """
             INSERT INTO DocumentTag (document_id, tag_id)
             VALUES (?, ?)
         """
        cursor.execute(sql, (document_id, tag_id))
        cursor.commit()
        print("插入成功")
        return True

    except Exception as e:
        print(f"插入文档标签时发生错误: {e}")
        # 发生错误时回滚事务
        cursor.rollback()
        return False


def new_JournalPos(cursor, document_id, journal_id, issue=None, page=None):
    try:
        sql = """
                INSERT INTO JournalPos (document_id,journal_id,issue,pages) 
            VALUES (?,?,?,?)
            """
        cursor.execute(sql, (document_id, journal_id, issue, page))
        cursor.commit()
        return True

    except Exception as e:
        print(f"插入期刊信息时发生错误: {e}")
        # 发生错误时回滚事务
        cursor.rollback()
        return False

def new_Upload(cursor, user_id, document_id):
    sql = """
            INSERT INTO Upload (user_id,document_id) 
        VALUES (?,?)
        """
    cursor.execute(sql, (user_id, document_id))
    cursor.commit()

#添加文件源
def new_filesrc(cursor,documentid,file_src):
    sql="""
        Insert into docsrc(document_id,src_url)
        VALUES (?,?)
        """
    cursor.execute(sql,(documentid,file_src))
    cursor.commit()

def new_filedata(cursor,documentid,file_data):
    sql="""
        Insert into docsrc(document_id,file_data)
        values(?,?)"""
    cursor.execute(sql,(documentid,file_data))
    cursor.commit()



######################################################
# 上传文件01
def upload_file(cursor, title, src, publicatio_date, user_id, author_id, tag_id, journal_id, issue, page):
    # 先插入document
    document_id = new_Document(cursor, title, publicatio_date, src)
    # 先插入document_author关系
    new_DocumentAuthor(cursor, document_id, author_id)
    # 再插入document_tag关系
    new_DocumentTag(cursor, document_id, tag_id)
    # 再插入journal_pos关系
    new_JournalPos(cursor, document_id, journal_id, issue, page)
    # 最后插入upload关系
    new_Upload(cursor, user_id, document_id)
    cursor.commit()
    return document_id


######################################################
# 各种查询函数

# 根据用户名跟密码查询用户是否存在，返回布尔值和用户id和用户权限等级
def login_query(cursor, username, password):
    cursor.execute("""
                SELECT password,user_id,permission FROM [User] WHERE username =?
                """, username)
    result = cursor.fetchone()
    if result is None:
        return (False, None,None)
    else:
        bool_result = result[0] == password
        userid = result[1]
        permission = result[2]
        return (bool_result, userid,permission)

def login_query_email(cursor, email, password):
    cursor.execute("""
                SELECT password,user_id,permission FROM [User] WHERE email =?
                """, email)
    result = cursor.fetchone()
    if result is None:
        return (False, None,None)
    else:
        bool_result = result[0] == password
        userid = result[1]
        permission = result[2]
        return (bool_result, userid,permission)

def query_all_Userinfo(cursor,user_id):
    try:
        cursor.execute("""
                SELECT * FROM [User] WHERE user_id = ?
                """, user_id)
        result = cursor.fetchone()
        if result is None:
            return (False, None)
        else:
            return (True, result)
    except Exception as e:
        print(f"Error: {e}")
        return (False, None)

def query_all_with_documentid(cursor,document_id):
    #文件基础信息
    cursor.execute("""
                SELECT * FROM Document WHERE document_id = ?
                """, document_id)
    docInfo = cursor.fetchone()
    if docInfo is None:
        return None

    #文档作者信息
    cursor.execute("""
    SELECT Author.Author_id,Author.name,DocumentAuthor.author_level from Document,DocumentAuthor,Author
    where Document.document_id = ? and Document.document_id = DocumentAuthor.document_id and DocumentAuthor.author_id = Author.author_id
    """, document_id)
    authorInfo = cursor.fetchall()

    #文档标签信息
    cursor.execute("""
    SELECT Tag.tag_id,Tag.name from Document,DocumentTag,Tag
    where Document.document_id = DocumentTag.document_id
    and DocumentTag.tag_id = Tag.tag_id
    and Document.document_id = ?
    """, document_id)
    tagInfo = cursor.fetchall()

    #文档期刊信息
    cursor.execute("""
    SELECT Journal.journal_id,Journal.name,JournalPos.issue,JournalPos.pages from Document,JournalPos,Journal
    where Document.document_id = JournalPos.document_id and JournalPos.journal_id = Journal.journal_id and Document.document_id = ?
    """, document_id)
    journalInfo = cursor.fetchone()
    return (docInfo, authorInfo, tagInfo, journalInfo)



def query_all_users(cursor):
    cursor.execute("""
                SELECT * FROM [User]
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_with_authorname(cursor, authorname):
    cursor.execute("""
                SELECT Document.document_id,Document.title, Author.name 
                FROM Document, DocumentAuthor, Author 
                WHERE Author.name LIKE ? AND 
                      Document.document_id = DocumentAuthor.document_id AND 
                      DocumentAuthor.author_id = Author.author_id
            """, (f'%{authorname}%',))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_with_title(cursor, title):
    cursor.execute("""
                SELECT Document.document_id,Document.title, Document.src_url FROM Document
                where Document.title like ?
                """, (f'%{title}%',))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_with_tag(cursor, tag):
    cursor.execute("""
                SELECT Document.document_id,Document.title, Document.src_url FROM Document, DocumentTag, Tag
                where Document.document_id = DocumentTag.document_id and DocumentTag.tag_id = Tag.tag_id and Tag.name like ?
                """, (f'%{tag}%',))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_all_authors(cursor):
    cursor.execute("""
                SELECT * FROM Author
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_all_documents(cursor):
    cursor.execute("""
                Select * From Document
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_all_tags(cursor):
    cursor.execute("""
                Select * From Tag
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_all_journals(cursor):
    cursor.execute("""
                Select * From Journal
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result

def query_with_journalname(cursor,journalname):
    cursor.execute("""
                Select Document.document_id,Document.title,Document.src_url From Document,JournalPos,Journal
                Where Document.document_id=JournalPos.document_id and JournalPos.journal_id=Journal.journal_id and Journal.name like ?
                """, (f'%{journalname}%',))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result



def query_all_document(cursor):
    cursor.execute("""
                Select * From Document
                """)
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_document_id(cursor, title):
    cursor.execute("""
                Select document_id From Document
                where title = ?
                """, (title,))
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        return result


def query_author_id(cursor, authorname):
    cursor.execute("""
                Select author_id From Author
                where name = ?
                """, (authorname,))
    result = cursor.fetchone()
    if result is None:
        return (False,None)
    else:
        return (True,result[0])


def query_tag_id(cursor, tagname):  # 返回一个tag_id
    cursor.execute("""
                Select tag_id From Tag
                where name = ?
                """, (tagname,))
    result = cursor.fetchone()
    if result is None:
        return (False,None)
    else:
        return (True,result[0])


def query_journal_id(cursor, journalname):  # 返回一个journal_id
    cursor.execute("""
                Select journal_id From Journal
                where name = ?
                """, (journalname))
    result = cursor.fetchone()
    if result is None:
        return (False,None)
    else:
        return (True,result[0])


def query_user_id(cursor, username):  # 返回一个user_id
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
# 删除关系
def delete_DocumentAuthor(cursor, document_id, author_id):
    try:
        cursor.execute("""
                DELETE FROM DocumentAuthor WHERE document_id = ? AND author_id = ?
            """, (document_id, author_id))
        # 提交事务
        cursor.commit()
        print("删除成功")
        return True

    except Exception as e:
        print(f"删除文档作者时发生错误: {e}")
        cursor.rollback()
        return False


def delete_DocumentTag(cursor, document_id, tag_id):
    try:
        cursor.execute("""
                  DELETE FROM DocumentTag WHERE document_id = ? AND tag_id = ?
                    """, (document_id, tag_id))
        cursor.commit()
        return True

    except Exception as e:
        print(f"删除文档标签时发生错误: {e}")
        cursor.rollback()
        return False


def delete_JournalPos(cursor, document_id, journal_id):
    try:
        cursor.execute("""
                    DELETE FROM JournalPos WHERE document_id = ? AND journal_id = ?
                    """, (document_id, journal_id))
        cursor.commit()
        return True
    except Exception as e:
        print(f"删除期刊信息时发生错误: {e}")
        cursor.rollback()
        return False

# 删除实体
def delete_Author(cursor, Author_id):
    cursor.execute("""
                DELETE FROM Author WHERE author_id = ?
                """, (Author_id,))
    cursor.commit()


def delete_Tag(cursor, Tag_id):
    cursor.execute("""
                DELETE FROM Tag WHERE tag_id = ?
                """, (Tag_id,))
    cursor.commit()


def delete_Journal(cursor, Journal_id):
    cursor.execute("""
                DELETE FROM Journal WHERE journal_id = ?
                """, (Journal_id,))
    cursor.commit()


def delete_User(cursor, User_id):
    delete_user_sql = "DELETE FROM [User] WHERE user_id = ?"
    cursor.execute(delete_user_sql, (User_id,))
    cursor.commit()

def delete_Document(cursor, Document_id):
    cursor.execute("""
                DELETE FROM Document WHERE document_id = ?
                """, (Document_id,))
    cursor.commit()

def delete_docsrc(cursor,document_id):
    cursor.execute("""
    DELETE FROM docsrc WHERE document_id = ?""",(document_id))
    cursor.commit()

################################################################
# 更新实体
def update_Author(cursor, author_id, name, email, affiliation):
    cursor.execute("""
                UPDATE Author SET name = ?, email = ?, affiliation = ? WHERE author_id = ?
                """, (name, email, affiliation, author_id))
    cursor.commit()

def update_Tag(cursor, tag_id, name):
    cursor.execute("""
                UPDATE Tag SET name = ? WHERE tag_id = ?
                """, (name, tag_id))
    cursor.commit()

def update_Journal(cursor, journal_id, name):
    cursor.execute("""
                UPDATE Journal SET name = ? WHERE journal_id = ?
                """, (name, journal_id))
    cursor.commit()

def update_JournalPos(cursor,document_id,journal_id,issue,page):
    try:
        cursor.execute("""
        UPDATE JournalPos SET issue = ?, pages = ? WHERE document_id = ? AND journal_id = ?
        """, (issue, page, document_id, journal_id))
        cursor.commit()
        return True
    except Exception as e:
        print(f"更新期刊信息时发生错误: {e}")
        cursor.rollback()
        return False

def update_User(cursor, username, user_id, password, email):
    try:
        cursor.execute("""
                        UPDATE [User] SET username = ?, password = ?, email = ? WHERE user_id = ?
                        """, (username, password, email, user_id))
        cursor.commit()
        return True
    except Exception as e:
        print(f"更新用户信息时发生错误: {e}")
        cursor.rollback()
        return False

def update_User_permission(cursor, user_id, permission):
    try:
        cursor.execute("""
           UPDATE [User] SET permission = ? WHERE user_id = ?
           """, (permission, user_id))
        cursor.commit()
        return True
    except Exception as e:
        print(f"更新用户权限时发生错误: {e}")
        cursor.rollback()
        return False


def update_Document(cursor, document_id, title, publication_date, src_url):
    cursor.execute("""
                UPDATE Document SET title = ?, publication_date = ?, src_url = ? WHERE document_id = ?
                """, (title, publication_date, src_url, document_id))
    cursor.commit()

def update_Document_src(cursor, document_id, src_url):
    try:
        cursor.execute("""
        UPDATE Document SET src_url = ? WHERE document_id = ?
        """, (src_url, document_id))
        cursor.commit()
        return True
    except Exception as e:
        print(f"更新文档源地址时发生错误: {e}")
        cursor.rollback()
        return False

def update_Document_srcdata(cursor, document_id, file_data):
    cursor.execute("""
    UPDATE docsrc SET file_data = ? WHERE document_id = ?
    """, (file_data, document_id))
    cursor.commit()

def update_Document_keywords(cursor, document_id, keywords):
    try:
        cursor.execute("""
        UPDATE Document SET keywords = ? WHERE document_id = ?
        """, (keywords, document_id))
        cursor.commit()
        return True

    except Exception as e:
        print(f"更新文档关键字时发生错误: {e}")
        cursor.rollback()
        return False


