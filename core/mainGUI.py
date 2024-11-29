import datetime
from tkinter import messagebox

from DB_Management.init_Cursor import *
import tkinter as tk
from DB_Management.query import *
from tkinter import ttk
from datetime import datetime

# 连接数据库,获取游标
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection


class queryGUI:
    def __init__(self,cursor,connection):
        self.cursor = cursor
        self.connection = connection

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("登录界面")
        self.root.geometry("900x600")

        self.Docname=tk.Entry(self.root)
        self.Docname.place(x=150,y=50,width=500,height=30)

        self.queryButton=tk.Button(self.root,text="查询",command=self.queryDoc)
        self.queryButton.place(x=100,y=50,width=50,height=30)

        #选择查询方式
        self.queryType = ttk.Combobox(self.root, values=["title", "author", "tag","journal"])
        self.queryType.set("title")  # 设置默认值
        self.queryType.place(x=50,y=50,width=50,height=30)

        # 创建用于显示查询结果的框架（容器）
        self.results_frame = tk.Frame(self.root)
        self.results_frame.place(x=150,y=100,width=500,height=400)

        # 运行主循环
        self.root.mainloop()

    def on_button_click(self, doc):
        # 这里定义按钮点击后的动作
        print(f"你点击了: {doc}")
        #####################################待补充##############
        #messagebox.showinfo("文档详情", f"你点击了: {doc}")
        (DocInfo,AuthorInfo,TagInfo,JournalInfo)=query_all_with_documentid(cursor,doc)
        print(DocInfo)
        print(AuthorInfo)
        print(TagInfo)
        print(JournalInfo)


    def queryDoc(self):
        inputKey=self.Docname.get()#获取输入的关键字
        querytype=self.queryType.get()
        result=[]
        if querytype== "title":
            result = query_with_title(cursor, inputKey)
        elif querytype== "author":
            result = query_with_authorname(cursor, inputKey)
        elif querytype== "tag":
            result = query_with_tag(cursor, inputKey)
        elif querytype== "journal":
            result = query_with_journalname(cursor, inputKey)

        #print(result)

        # 清空之前显示的结果
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # 为查询结果中的每个项生成一个按钮
        for i, doc in enumerate(result):
            button = tk.Button(self.results_frame,relief='solid',borderwidth=1, text=doc[1],anchor="w", command=lambda doct=doc: self.on_button_click(doct[0]))
            button.place(x=0,y=i*50,width=500,height=50)


class AddDocGUI:
    def __init__(self,cursor,connection):
        self.cursor = cursor
        self.connection = connection

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("添加文档")
        self.root.geometry("900x600")

        self.ConfirmButton=tk.Button(self.root,text="确认添加",command=self.addDoc)
        self.ConfirmButton.place(x=50,y=50,width=50,height=30)

        self.Label1=tk.Label(self.root,text="文档名称：")
        self.Label1.place(x=150,y=60,width=100,height=40)
        self.Docname=tk.Entry(self.root)
        self.Docname.place(x=150,y=100,width=250,height=50)

        self.Label7=tk.Label(self.root,text="文档关键词：")
        self.Label7.place(x=450,y=60,width=100,height=40)
        self.DocKeywords=tk.Entry(self.root)
        self.DocKeywords.place(x=450, y=100, width=400, height=50)

        self.Label2=tk.Label(self.root,text="文档第一作者,有多个请用英文逗号隔开",anchor="w")
        self.Label2.place(x=150,y=160,width=200,height=40)
        self.Docauthor01=tk.Entry(self.root)
        self.Docauthor01.place(x=150,y=200,width=300,height=50)

        self.Label8=tk.Label(self.root,text="发表日期，yyyy-MM-dd",anchor="w")
        self.Label8.place(x=500,y=160,width=200,height=40)
        self.Docdate=tk.Entry(self.root)
        self.Docdate.place(x=500,y=200,width=300,height=50)
        today_date = datetime.today().strftime('%Y-%m-%d')
        self.Docdate.insert(0, today_date)

        self.Label3=tk.Label(self.root,text="文档第二作者，有多个请用英文逗号隔开",anchor="w")
        self.Label3.place(x=150,y=260,width=200,height=40)
        self.Docauthor02=tk.Entry(self.root)
        self.Docauthor02.place(x=150,y=300,width=300,height=50)


        self.Label4=tk.Label(self.root,text="文档标签，有多个请用英文逗号隔开",anchor="w")
        self.Label4.place(x=150,y=360,width=200,height=40)
        self.Doctag=tk.Entry(self.root)
        self.Doctag.place(x=150,y=400,width=250,height=50)

        self.Label9=tk.Label(self.root,text="src",anchor="w")
        self.Label9.place(x=450,y=360,width=200,height=40)
        self.Docsrc=tk.Entry(self.root)
        self.Docsrc.place(x=450,y=400,width=250,height=50)

        self.Label5=tk.Label(self.root,text="文档期刊名称",anchor="w")
        self.Label5.place(x=150,y=460,width=100,height=40)
        self.Docjournalname=tk.Entry(self.root)
        self.Docjournalname.place(x=150,y=500,width=200,height=50)

        self.Label6=tk.Label(self.root,text="期刊期号",anchor="w")
        self.Label6.place(x=400,y=460,width=100,height=40)
        self.JournalIssue=tk.Entry(self.root)
        self.JournalIssue.place(x=400,y=500,width=200,height=50)
        
        self.Label10=tk.Label(self.root,text="期刊页数",anchor="w")
        self.Label10.place(x=650,y=460,width=100,height=40)
        self.JournalPages=tk.Entry(self.root)
        self.JournalPages.place(x=650,y=500,width=200,height=50)



        # 运行主循环
        self.root.mainloop()

    def addDoc(self):
        docname=self.Docname.get()
        doctag=self.Doctag.get()
        docJournalname=self.Docjournalname.get()
        docauthor01=self.Docauthor01.get()
        docauthor02=self.Docauthor02.get()
        JournalIssue=self.JournalIssue.get()
        docdate=self.Docdate.get()
        dockeywords=self.DocKeywords.get()
        docsrc=self.Docsrc.get()
        JournalPages=self.JournalPages.get()

        print(docdate)

        # 处理作者信息和标签信息
        authorlist01=docauthor01.split(",")
        authorlist02=docauthor02.split(",")
        taglist=doctag.split(",")

        authoridlist01=[]
        authoridlist02=[]
        tagidlist=[]
        #检测作者表中是否存在该作者，不存在则插入
        for author in authorlist01:
            if author == "":
                continue
            (res,id)=query_author_id(cursor,author)
            if res==False:
                authoridlist01.append(new_Author(cursor,author))
            else:
                authoridlist01.append(id)
        for author in authorlist02:
            if author == "":
                continue
            (res,id)=query_author_id(cursor,author)
            if res==False:
                authoridlist02.append(new_Author(cursor,author))
            else:
                authoridlist02.append(id)

        print(authoridlist01)
        print(authoridlist02)

        #检测标签表中是否存在该标签，不存在则插入
        for tag in taglist:
            if tag == "":
                continue
            (res,id)=query_tag_id(cursor,tag)
            if res==False:
                tagidlist.append(new_Tag(cursor,tag))
            else:
                tagidlist.append(id)

        #print(tagidlist)

        #journalid
        journalid=-1;
        (res,id)=query_journal_id(cursor,docJournalname)
        if not res:
            journalid=new_Journal(cursor,docJournalname)
        print(journalid)

        #新建文档
        documentid=new_Document(cursor,docname,docdate,docsrc,dockeywords);
        print(documentid)
        documentid=int(documentid)
        print(type(documentid))

        #插入作者信息
        for authorid in authoridlist01:
            if authorid == "":
                continue
            print(type(authorid))
            new_DocumentAuthor(cursor,documentid,authorid,1)
        for authorid in authoridlist02:
            if authorid == "":
                continue
            new_DocumentAuthor(cursor,documentid,authorid,2)
        #插入标签信息
        for tagid in tagidlist:
            if authorid == "":
                continue
            new_DocumentTag(cursor,documentid,tagid)
        #插入期刊信息
        new_JournalPos(cursor,documentid,journalid,JournalIssue,JournalPages)


        tk.messagebox.showinfo("提示", "添加成功！")












# 创建并运行GUI
if __name__ == "__main__":
    queryGUI(cursor, connection)







