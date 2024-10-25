import pyodbc
from init_Cursor import init_Cursor

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
