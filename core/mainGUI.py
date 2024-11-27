from tkinter import messagebox

from DB_Management.init_Cursor import *
import tkinter as tk
from DB_Management.query import *

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

        # 创建用于显示查询结果的框架（容器）
        self.results_frame = tk.Frame(self.root)
        self.results_frame.place(x=150,y=100,width=500,height=400)

        # 运行主循环
        self.root.mainloop()

    def on_button_click(self, doc):
        # 这里定义按钮点击后的动作
        print(f"你点击了: {doc}")
        # 可以在这里添加更多的逻辑，比如打开文档等
        # 例如，你可以用一个弹窗显示更多的文档信息
        messagebox.showinfo("文档详情", f"你点击了: {doc}")

    def queryDoc(self):
        docname=self.Docname.get()
        result=query_with_title(cursor,docname)
        print(result)

        # 清空之前显示的结果
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # 为查询结果中的每个项生成一个按钮
        for i, doc in enumerate(result):
            button = tk.Button(self.results_frame,relief='solid',borderwidth=1, text=doc[0],anchor="w", command=lambda doct=doc: self.on_button_click(doc[1]))
            button.place(x=0,y=i*50,width=500,height=50)



# 创建并运行GUI
if __name__ == "__main__":
    queryGUI(cursor, connection)







