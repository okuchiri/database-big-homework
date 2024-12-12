import tkinter as tk
from tkinter import messagebox
from DB_Management.query import *
from DB_Management.init_Cursor import init_Cursor


# 连接数据库,获取游标
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection

class LoginRegisterGui:
    def __init__(self,cursor,connection):
        self.cursor = cursor
        self.connection = connection
        self.user_id=None
        self.permission=None

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("登录界面")
        self.root.geometry("600x400")

        # 两个页面，登录页面和注册页面
        self.loginpage = tk.Frame(self.root)
        self.registerpage = tk.Frame(self.root)

        # 登录界面
        # 创建标签和文本框
        self.label_username = tk.Label(self.loginpage, text="用户名:")
        self.label_username.place(x=50, y=100)

        self.entry_username = tk.Entry(self.loginpage)
        self.entry_username.place(x=50, y=150)

        self.label_password = tk.Label(self.loginpage, text="密码:")
        self.label_password.place(x=50, y=200)

        self.entry_password = tk.Entry(self.loginpage, show='*')
        self.entry_password.place(x=50, y=250)

        # 创建登录按钮
        login_button = tk.Button(self.loginpage, text="登录", command=self.login)
        login_button.place(x=50, y=300, width=60, height=30)

        # 注册按钮
        register_button = tk.Button(self.loginpage, text="注册", command=self.show_register_page)
        register_button.place(x=150, y=300, width=60, height=30)

        # 关闭按钮
        cancel_button = tk.Button(self.loginpage, text="关闭", command=self.root.quit)
        cancel_button.place(x=250, y=300, width=60, height=30)

        # 注册界面
        # 创建标签和文本框
        self.label_register_username = tk.Label(self.registerpage, text="用户名:")
        self.label_register_username.place(x=50, y=100)

        self.register_username = tk.Entry(self.registerpage)
        self.register_username.place(x=50, y=150)

        self.label_register_password = tk.Label(self.registerpage, text="密码:")
        self.label_register_password.place(x=50, y=200)

        self.register_password = tk.Entry(self.registerpage, show='*')
        self.register_password.place(x=50, y=250)

        # 创建确认按钮
        confirm_button = tk.Button(self.registerpage, text="确认", command=self.register)
        confirm_button.place(x=50, y=300, width=60, height=30)

        # 关闭按钮
        cancel_button = tk.Button(self.registerpage, text="返回", command=self.show_login_page)
        cancel_button.place(x=250, y=300, width=60, height=30)

        # 显示登录页面
        self.show_login_page()

        # 运行主循环
        self.root.mainloop()

    def show_login_page(self):
        self.registerpage.forget()
        self.loginpage.pack(fill="both", expand=True)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        result, userid, permission = login_query(self.cursor, username, password)

        if result:
            messagebox.showinfo("登录成功", f"欢迎，{username}！")
            # print(userid)
            # print(permission)
            self.user_id = userid
            self.permission = permission
            self.root.destroy()

        else:
            messagebox.showwarning("登录失败", "用户名或密码错误")

    def show_register_page(self):
        self.loginpage.forget()
        self.registerpage.pack(fill="both", expand=True)

    def register(self):
        username = self.register_username.get()
        password = self.register_password.get()
        if username == "" or password == "":
            messagebox.showwarning("注册失败", "用户名或密码不能为空！")
        else:
            result, userid = new_User(self.cursor, username, password)

            if result:
                messagebox.showinfo("注册成功", "注册成功！")
                self.show_login_page()
            else:
                messagebox.showwarning("注册失败", "用户名已存在")

    def get_User_info(self):
        return self.user_id, self.permission

# 创建并运行GUI
if __name__ == "__main__":
    LoginRegisterGui(cursor, connection)
