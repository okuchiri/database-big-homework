import tkinter as tk
from tkinter import messagebox
from DB_Management.query import *
from DB_Management.init_Cursor import init_Cursor


# 连接数据库,获取游标
DBCONNECTOR=init_Cursor
DBCONNECTOR.__init__(DBCONNECTOR)
cursor=DBCONNECTOR.cursor
connection=DBCONNECTOR.connection


def show_login_page():
    registerpage.forget()
    loginpage.pack(fill="both", expand=True)


def login():
    username = entry_username.get()
    password = entry_password.get()

    (result,userid)=login_query(cursor,username,password)

    if(result):
        messagebox.showinfo("登录成功", "欢迎，" + username + "！")
    else:
        messagebox.showwarning("登录失败", "用户名或密码错误")

def show_register_page():
    loginpage.forget()
    registerpage.pack(fill="both", expand=True)

def register():
    username=register_username.get()
    password=register_password.get()
    (result,userid)=new_User(cursor,username,password)

    if(result):
        messagebox.showinfo("注册成功", "注册成功！")
        show_login_page()
    else:
        messagebox.showwarning("注册失败", "用户名已存在")


#创建主窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("600x400")

#两个页面，登录页面和注册页面
loginpage=tk.Frame(root)
registerpage=tk.Frame(root)

# 登录界面
# 创建标签和文本框
label_username = tk.Label(loginpage, text="用户名:")
label_username.place(x=50,y=100)

entry_username = tk.Entry(loginpage)
entry_username.place(x=50,y=150)

label_password = tk.Label(loginpage, text="密码:")
label_password.place(x=50,y=200)

entry_password = tk.Entry(loginpage, show='*')
entry_password.place(x=50,y=250)

# 创建登录按钮
login_button = tk.Button(loginpage, text="登录", command=login)
login_button.place(x=50,y=300,width=60,height=30)

# 注册按钮
register_button=tk.Button(loginpage,text="注册",command=show_register_page)
register_button.place(x=150,y=300,width=60,height=30)
#关闭按钮
cancel_button = tk.Button(loginpage, text="关闭", command=root.quit)
cancel_button.place(x=250,y=300,width=60,height=30)


# 注册界面
# 创建标签和文本框
label_username = tk.Label(registerpage, text="用户名:")
label_username.place(x=50,y=100)

register_username = tk.Entry(registerpage)
register_username.place(x=50,y=150)

label_password = tk.Label(registerpage, text="密码:")
label_password.place(x=50,y=200)

register_password = tk.Entry(registerpage, show='*')
register_password.place(x=50,y=250)

# 创建确认按钮
confirm_button = tk.Button(registerpage, text="确认", command=register)
confirm_button.place(x=50,y=300,width=60,height=30)

#关闭按钮
cancel_button = tk.Button(registerpage, text="返回", command=show_login_page)
cancel_button.place(x=250,y=300,width=60,height=30)

# 显示登录页面
show_login_page()


# 运行主循环
root.mainloop()
