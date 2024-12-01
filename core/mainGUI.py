import datetime
from contextlib import nullcontext
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
        # (DocInfo,AuthorInfo,TagInfo,JournalInfo)=query_all_with_documentid(cursor,doc)
        # print(DocInfo)
        # print(AuthorInfo)
        # print(TagInfo)
        # print(JournalInfo)

        ShowDetailGui(self.cursor,self.connection,doc)



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


class ShowDetailGui:

    def __init__(self,cursor,connection,DocID):
        self.cursor = cursor
        self.connection = connection
        self.DocID=DocID

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("文档详情")
        self.root.geometry("900x600")
        # 显示文档信息
        (DocInfo,AuthorInfo,TagInfo,JournalInfo)=query_all_with_documentid(cursor,self.DocID)
        print(DocInfo)
        print(AuthorInfo)
        print(TagInfo)
        print(JournalInfo)

        self.Label1=tk.Label(self.root,text="文档名称："+DocInfo[1],anchor='w')
        self.Label1.place(x=150,y=50,width=500,height=50)

        KeywordLabel="文档关键词："
        if(DocInfo[4]!=None):
            KeywordLabel+=DocInfo[4]
        else:
            KeywordLabel+="无"
        self.Label2=tk.Label(self.root,text=KeywordLabel,anchor='w')
        self.Label2.place(x=150,y=100,width=500,height=50)

        AuthorLabel01=""
        for author in AuthorInfo:
            if author[2]==1:
                AuthorLabel01+=author[1]
                AuthorLabel01+=','
        AuthorLabel02=""
        for author in AuthorInfo:
            if author[2]!=2:
                AuthorLabel02+=author[1]
                AuthorLabel02+=','

        self.Label3=tk.Label(self.root,text="文档第一作者："+AuthorLabel01,anchor='w')
        self.Label3.place(x=150,y=150,width=500,height=40)
        self.Label4=tk.Label(self.root,text="文档第二作者："+AuthorLabel02,anchor='w')
        self.Label4.place(x=150,y=200,width=500,height=40)

        TagLabel=""
        for tag in TagInfo:
            TagLabel+=tag[1]
            TagLabel+=','
        self.Label5=tk.Label(self.root,text="文档标签："+TagLabel,anchor='w')
        self.Label5.place(x=150,y=250,width=500,height=40)

        docsrc="文档来源："
        if docsrc!=None:
            docsrc+=str(DocInfo[3])
        else:
            docsrc+="无"
        self.Label6=tk.Label(self.root,text=docsrc,anchor='w')
        self.Label6.place(x=150,y=300,width=500,height=40)

        formatted_date = DocInfo[2].strftime('%Y-%m-%d')
        self.Label7 = tk.Label(self.root, text=f"文档发表日期：{formatted_date}", anchor='w')
        self.Label7.place(x=150,y=350,width=500,height=40)

        JournalLabel="期刊名称："
        if JournalInfo!=None and JournalInfo[1]!=None:
            JournalLabel+=JournalInfo[1]
        else:
            JournalLabel+="无"
        self.Label8=tk.Label(self.root,text=JournalLabel,anchor='w')
        self.Label8.place(x=150,y=400,width=500,height=40)

        JournalissueLabel="期刊期号："
        if JournalInfo!=None and JournalInfo[2]!=None:
            JournalissueLabel+=JournalInfo[2]
        else:
            JournalissueLabel+="无"
        self.Label9=tk.Label(self.root,text=JournalissueLabel,anchor='w')
        self.Label9.place(x=150,y=450,width=500,height=40)

        JournalPagesLabel="期刊页数："
        if JournalInfo!=None and JournalInfo[3]!=None:
            JournalPagesLabel+=JournalInfo[3]
        else:
            JournalPagesLabel+="无"
        self.Label10=tk.Label(self.root,text=JournalPagesLabel,anchor='w')
        self.Label10.place(x=150,y=500,width=500,height=40)

        # 运行主循环
        self.root.mainloop()

class EditDocGUI:
    def __init__(self,cursor,connection,DocID):
        self.cursor = cursor
        self.connection = connection
        self.DocID=DocID

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("编辑文档")
        self.root.geometry("900x600")

        #3个页面
        self.mainpage=tk.Frame(self.root)
        self.editAuthorPage=tk.Frame(self.root)
        self.editTagPage=tk.Frame(self.root)

        # 显示文档信息
        (DocInfo, AuthorInfo, TagInfo, JournalInfo) = query_all_with_documentid(cursor, self.DocID)

        self.DocInfo=DocInfo
        self.AuthorInfo=AuthorInfo
        self.TagInfo=TagInfo
        self.JournalInfo=JournalInfo

        self.Label1 = tk.Label(self.mainpage, text="文档名称：", anchor='w')
        self.Label1.place(x=50, y=50, width=100, height=50)
        self.NameLabel = tk.Label(self.mainpage, text=DocInfo[1], anchor='w')
        self.NameLabel.place(x=50, y=100, width=500, height=50)

        Keywords = ""
        if (DocInfo[4] != None):
            Keywords += DocInfo[4]
        else:
            Keywords += "无"
        self.Label2 = tk.Label(self.mainpage, text="文档关键词：", anchor='w')
        self.Label2.place(x=50, y=150, width=100, height=50)
        self.KeywordEntry = tk.Entry(self.mainpage)
        self.KeywordEntry.place(x=50, y=200, width=500, height=50)
        self.KeywordEntry.insert(0, Keywords)

        self.KeywordButton=tk.Button(self.mainpage,text="修改关键词",anchor='w',command=self.editKeyword)
        self.KeywordButton.place(x=600, y=200, width=100, height=50)

        AuthorLabel01 = ""
        for author in AuthorInfo:
            if author[2] == 1:
                AuthorLabel01 += author[1]
                AuthorLabel01 += ','
        AuthorLabel02 = ""
        for author in AuthorInfo:
            if author[2] != 2:
                AuthorLabel02 += author[1]
                AuthorLabel02 += ','

        self.Label3 = tk.Label(self.mainpage, text="文档第一作者：" + AuthorLabel01, anchor='w')
        self.Label3.place(x=50, y=300, width=400, height=40)
        self.Label4 = tk.Label(self.mainpage, text="文档第二作者：" + AuthorLabel02, anchor='w')
        self.Label4.place(x=50, y=350, width=400, height=40)

        TagLabel = ""
        for tag in TagInfo:
            TagLabel += tag[1]
            TagLabel += ','
        self.Label5 = tk.Label(self.mainpage, text="文档标签：" + TagLabel, anchor='w')
        self.Label5.place(x=50, y=400, width=500, height=40)

        self.Label6=tk.Label(self.mainpage,text="修改作者",anchor='w')
        self.Label6.place(x=500, y=300, width=500, height=40)
        self.authorButton=tk.Button(self.mainpage,text="修改作者",anchor='w',command=self.editAuthor)
        self.authorButton.place(x=600, y=300, width=60, height=40)

        self.Label7=tk.Label(self.mainpage,text="修改标签",anchor='w')
        self.Label7.place(x=500, y=350, width=500, height=40)
        self.tagButton=tk.Button(self.mainpage,text="修改标签",anchor='w',command=self.editTag)
        self.tagButton.place(x=600, y=350, width=60, height=40)

        docsrc = ""
        if docsrc != None:
            docsrc += str(DocInfo[3])
        else:
            docsrc += "无"
        self.Label6 = tk.Label(self.mainpage, text="文档来源：", anchor='w')
        self.Label6.place(x=50, y=450, width=100, height=40)
        self.Docsrcentry=tk.Entry(self.mainpage)
        self.Docsrcentry.place(x=50, y=500, width=300, height=50)
        self.Docsrcentry.insert(0, docsrc)

        self.srcConfirmButton=tk.Button(self.mainpage,text="确认修改",anchor='w',command=self.docsrcEdit)
        self.srcConfirmButton.place(x=150, y=450, width=70, height=40)

        JournalLabel =""
        if JournalInfo != None and JournalInfo[1] != None:
            JournalLabel += JournalInfo[1]
        else:
            JournalLabel += "无"
        self.Label8 = tk.Label(self.mainpage, text="期刊名称", anchor='w')
        self.Label8.place(x=400, y=400, width=70, height=40)
        self.JournalnameEntry = tk.Entry(self.mainpage)
        self.JournalnameEntry.place(x=470, y=400, width=300, height=50)
        self.JournalnameEntry.insert(0, JournalLabel)

        JournalissueLabel = ""
        if JournalInfo != None and JournalInfo[2] != None:
            JournalissueLabel += JournalInfo[2]
        else:
            JournalissueLabel += "无"
        self.Label9 = tk.Label(self.mainpage, text="期刊期号：", anchor='w')
        self.Label9.place(x=400, y=450, width=70, height=40)
        self.JournalissueEntry = tk.Entry(self.mainpage)
        self.JournalissueEntry.place(x=470, y=450, width=300, height=50)
        self.JournalissueEntry.insert(0, JournalissueLabel)


        JournalPagesLabel = ""
        if JournalInfo != None and JournalInfo[3] != None:
            JournalPagesLabel += JournalInfo[3]
        else:
            JournalPagesLabel += "无"
        self.Label10 = tk.Label(self.mainpage, text="期刊页数：", anchor='w')
        self.Label10.place(x=400, y=500, width=70,height=40)

        self.JournalPagesEntry = tk.Entry(self.mainpage)
        self.JournalPagesEntry.place(x=470, y=500, width=150, height=50)
        self.JournalPagesEntry.insert(0, JournalPagesLabel)

        self.JournalPagesButton=tk.Button(self.mainpage,text="修改期刊信息",anchor='w',command=self.editJournal)
        self.JournalPagesButton.place(x=650, y=500, width=100, height=50)

        self.mainpage.pack(fill="both", expand=True)
        self.editTagPage.forget()
        self.editAuthorPage.forget()

        self.root.mainloop()

    def editJournal(self):
        journalname=self.JournalnameEntry.get()
        journalissue=self.JournalissueEntry.get()
        journalpages=self.JournalPagesEntry.get()

        tempjournalid=-1
        (res,id)=query_journal_id(cursor,journalname)
        if not res:
            tempjournalid=new_Journal(cursor,journalname)
        else:
            tempjournalid=id

        if self.JournalInfo is not None and tempjournalid == self.JournalInfo[0]:
            result=update_JournalPos(cursor,self.DocID,tempjournalid,journalissue,journalpages)
            if(result):
                tk.messagebox.showinfo("提示", "修改成功！")
            else:
                tk.messagebox.showinfo("提示", "修改失败！")
        else:
            if self.JournalInfo is not None:
                result=delete_JournalPos(cursor,self.DocID,self.JournalInfo[0])
            else:
                result=True
            if(result):
                result=new_JournalPos(cursor,self.DocID,tempjournalid,journalissue,journalpages)
                if(result):
                    tk.messagebox.showinfo("提示", "修改成功！")
                else:
                    tk.messagebox.showinfo("提示", "修改失败！")
            else:
                tk.messagebox.showinfo("提示", "修改失败！")


    def docsrcEdit(self):
        newsrc=self.Docsrcentry.get()
        result=update_Document_src(cursor,self.DocID,newsrc)
        if(result):
            tk.messagebox.showinfo("提示", "修改成功！")
        else:
            tk.messagebox.showinfo("提示", "修改失败！")

    def editKeyword(self):
        newKeyword=self.KeywordEntry.get()
        result=update_Document_keywords(cursor,self.DocID,newKeyword)
        if(result):
            tk.messagebox.showinfo("提示", "修改成功！")
        else:
            tk.messagebox.showinfo("提示", "修改失败！")

    def backToMain(self):
        self.editAuthorPage.forget()
        self.editTagPage.forget()
        self.mainpage.pack(fill="both", expand=True)

    def editAuthor(self):
        self.editAuthorPage.pack(fill="both", expand=True)
        self.editTagPage.forget()
        self.mainpage.forget()

        self.returnButton=tk.Button(self.editAuthorPage,text="返回",anchor='w',command=self.backToMain)
        self.returnButton.place(x=50, y=50, width=100, height=50)

        self.Label8=tk.Label(self.editAuthorPage,text="作者名称：",anchor='w')
        self.Label8.place(x=50, y=150, width=100, height=50)
        self.authorEntry=tk.Entry(self.editAuthorPage)
        self.authorEntry.place(x=50, y=200, width=200, height=50)

        self.Label9=tk.Label(self.editAuthorPage,text="作者类型：",anchor='w')
        self.Label9.place(x=50, y=250, width=100, height=50)
        self.authorType = ttk.Combobox(self.root, values=["第一作者", "第二作者","其他"])
        self.authorType.set("第一作者")  # 设置默认值
        self.authorType.place(x=50, y=300, width=100, height=30)

        self.addAuthorButton=tk.Button(self.editAuthorPage,text="添加作者",anchor='w',command=self.addAuthor)
        self.addAuthorButton.place(x=50, y=350, width=100, height=50)

        self.deleteAuthorButton=tk.Button(self.editAuthorPage,text="删除作者",anchor='w',command=self.deleteAuthor)
        self.deleteAuthorButton.place(x=200, y=350, width=100, height=50)

    def addAuthor(self):
        authorname=self.authorEntry.get()
        authortype=self.authorType.get()
        if authorname=="":
            tk.messagebox.showinfo("提示", "作者名称不能为空！")
            return
        if authortype=="第一作者":
            authortype=1
        elif authortype=="第二作者":
            authortype=2
        else:
            authortype=3

        authorid=-1
        (res,id)=query_author_id(cursor,authorname)
        if not res:
            authorid=new_Author(cursor,authorname)
        else:
            authorid=id

        result= new_DocumentAuthor(cursor,self.DocID,authorid,authortype)
        if(result):
            tk.messagebox.showinfo("提示", "添加成功！")
        else:
            tk.messagebox.showinfo("提示", "添加失败,作者已存在！")

    def deleteAuthor(self):
        authorname=self.authorEntry.get()
        if authorname == "":
            tk.messagebox.showinfo("提示", "作者名称不能为空！")
            return
        authorid = -1
        (res, id) = query_author_id(cursor, authorname)
        if not res:
            authorid = new_Author(cursor, authorname)
        else:
            authorid = id

        result = delete_DocumentAuthor(cursor, self.DocID, authorid)

        if(result):
            tk.messagebox.showinfo("提示", "删除成功！")
        else:
            tk.messagebox.showinfo("提示", "删除失败！")


    def editTag(self):
        self.editTagPage.pack(fill="both", expand=True)
        self.editAuthorPage.forget()
        self.mainpage.forget()

        self.returnButton=tk.Button(self.editTagPage,text="返回",anchor='w',command=self.backToMain)
        self.returnButton.place(x=50, y=50, width=100, height=50)

        self.Label10=tk.Label(self.editTagPage,text="标签名称：",anchor='w')
        self.Label10.place(x=50, y=150, width=100, height=50)
        self.tagEntry=tk.Entry(self.editTagPage)
        self.tagEntry.place(x=50, y=200, width=200, height=50)

        self.addTagButton=tk.Button(self.editTagPage,text="添加标签",anchor='w',command=self.addTag)
        self.addTagButton.place(x=50, y=350, width=100, height=50)

        self.deleteTagButton=tk.Button(self.editTagPage,text="删除标签",anchor='w',command=self.deleteTag)
        self.deleteTagButton.place(x=200, y=350, width=100, height=50)



    def addTag(self):
        tagname=self.tagEntry.get()
        tagid=-1

        (result,tagres)=query_tag_id(cursor,tagname)
        if not result:
            tagid=new_Tag(cursor,tagname)
        else:
            tagid=tagres

        result=new_DocumentTag(cursor,self.DocID,tagid)
        if(result):
            tk.messagebox.showinfo("提示", "添加成功！")
        else:
            tk.messagebox.showinfo("提示", "添加失败,标签已存在！")


    def deleteTag(self):
        tagname=self.tagEntry.get()
        tagid = -1
        (result, tagres) = query_tag_id(cursor, tagname)
        if not result:
            tk.messagebox.showinfo("提示", "标签不存在！")
            return
        else:
            tagid = tagres
        result = delete_DocumentTag(cursor, self.DocID, tagid)
        if(result):
            tk.messagebox.showinfo("提示", "删除成功！")
        else:
            tk.messagebox.showinfo("提示", "删除失败！")


# 创建并运行GUI
if __name__ == "__main__":
    EditDocGUI(cursor, connection,1)







