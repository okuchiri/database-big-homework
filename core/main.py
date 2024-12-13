from LoginGUI import LoginRegisterGui
from DB_Management.init_Cursor import init_Cursor
from mainGUI import *
# 连接数据库,获取游标
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection

ADMIN_LEVEL=1000

#主界面
class MainGUI():
    def __init__(self, cursor, connection, UserID, UserLevel):
        self.cursor = cursor
        self.connection = connection
        self.UserID = UserID
        self.UserLevel = UserLevel
        self.root = tk.Tk()
        self.root.title("文献管理系统")
        self.root.geometry("900x600")

        self.homepage = tk.Frame(self.root)
        self.accountpage=tk.Frame(self.root)
        self.adminpage=tk.Frame(self.root)

        # 进入查询界面
        querybutton = tk.Button(self.homepage, text="查询", command=lambda: queryGUI(cursor, connection, UserLevel))
        querybutton.place(x=100, y=100, width=100, height=50)

        # 更改账户信息界面
        accountbutton = tk.Button(self.homepage, text="更改账户信息", command=self.accountInfo)
        accountbutton.place(x=250, y=100, width=100, height=50)

        #管理员界面
        adminbutton = tk.Button(self.homepage, text="管理员界面", command=self.adminPage)
        adminbutton.place(x=400, y=100, width=100, height=50)

        #上传文献界面
        uploadbutton = tk.Button(self.homepage, text="上传文献", command=lambda: AddDocGUI(cursor, connection))
        uploadbutton.place(x=550, y=100, width=100, height=50)

        #退出界面
        exitbutton = tk.Button(self.homepage, text="退出", command=self.root.quit)
        exitbutton.place(x=50, y=500, width=100, height=50)

        self.homepage.pack(fill=tk.BOTH, expand=True)
        self.accountpage.forget()
        self.adminpage.forget()

        self.root.mainloop()

    def returnHomepage(self):
        #切换页面
        self.accountpage.forget()
        self.adminpage.forget()
        self.homepage.pack(fill=tk.BOTH, expand=True)

    def accountInfo(self):
        #切换页面
        self.homepage.forget()
        self.adminpage.forget()
        self.accountpage.pack(fill=tk.BOTH, expand=True)

        (result,UserInfo)=query_all_Userinfo(self.cursor,self.UserID)
        if not result:
            print("查询账户信息失败")
            return
        # 账户信息界面
        self.UsernameLabel= tk.Label(self.accountpage, text="用户名：")
        self.UsernameLabel.place(x=100, y=100, width=100, height=50)
        self.UsernameinfoLabel=tk.Label(self.accountpage,text=""+str(UserInfo[1]),anchor=tk.W)
        self.UsernameinfoLabel.place(x=200, y=100, width=250, height=50)

        self.UserIDLabel=tk.Label(self.accountpage,text="用户ID："+str(UserInfo[0]),anchor=tk.W)
        self.UserIDLabel.place(x=450, y=100, width=100, height=50)

        self.PasswordLabel= tk.Label(self.accountpage, text="密码：")
        self.PasswordLabel.place(x=100, y=200, width=100, height=50)
        self.PasswordEntry= tk.Entry(self.accountpage)
        self.PasswordEntry.place(x=250, y=200, width=300, height=50)
        self.PasswordEntry.insert(0,UserInfo[3])

        self.emailLabel= tk.Label(self.accountpage, text="邮箱：")
        self.emailLabel.place(x=100, y=300, width=100, height=50)
        self.emailEntry= tk.Entry(self.accountpage)
        self.emailEntry.place(x=250, y=300, width=300, height=50)
        if UserInfo[2] is None:
            self.emailEntry.insert(0,"")
        else:
            self.emailEntry.insert(0,UserInfo[2])

        self.permissionLabel= tk.Label(self.accountpage, text="权限等级："+str(UserInfo[4]),anchor=tk.W)
        self.permissionLabel.place(x=100, y=400, width=100, height=50)

        self.returnbutton = tk.Button(self.accountpage, text="返回", command=self.returnHomepage)
        self.returnbutton.place(x=100, y=500, width=100, height=50)

        self.savebutton = tk.Button(self.accountpage, text="保存", command=self.saveAccountInfo)
        self.savebutton.place(x=250, y=500, width=100, height=50)

    def adminPage(self):
        if(self.UserLevel<ADMIN_LEVEL):
            tk.messagebox.showerror(title="错误", message="您没有权限访问管理员界面！")
            return

        #管理员界面
        self.homepage.forget()
        self.accountpage.forget()
        self.adminpage.pack(fill=tk.BOTH, expand=True)

        #返回主界面按钮
        self.returnbutton = tk.Button(self.adminpage, text="返回", command=self.returnHomepage)
        self.returnbutton.place(x=50, y=500, width=100, height=50)

        #更改用户权限
        self.label1=tk.Label(self.adminpage,text="请输入要修改的用户ID：",anchor=tk.W)
        self.label1.place(x=100, y=100, width=200, height=50)
        self.useridentry=tk.Entry(self.adminpage)
        self.useridentry.place(x=300, y=100, width=300, height=50)

        self.label2=tk.Label(self.adminpage,text="请输入新的权限等级：",anchor=tk.W)
        self.label2.place(x=100, y=200, width=200, height=50)
        self.permissionentry=tk.Entry(self.adminpage)
        self.permissionentry.place(x=300, y=200, width=300, height=50)

        self.changepermissionbutton=tk.Button(self.adminpage,text="修改权限",command=self.changePermission)
        self.changepermissionbutton.place(x=650, y=200, width=100, height=50)

    def changePermission(self):
        #修改用户权限
        userid = self.useridentry.get()
        permission = self.permissionentry.get()

        if userid == "" or permission == "":
            tk.messagebox.showerror(title="错误", message="用户ID或权限等级不能为空！")
            return
        #先查询用户是否存在
        (resulttmp,userinfo)=query_all_Userinfo(self.cursor,userid)
        if userinfo is None:
            tk.messagebox.showerror(title="错误", message="用户不存在！")
            return

        result=update_User_permission(self.cursor,userid,permission)
        if result:
            tk.messagebox.showinfo(title="成功", message="用户权限修改成功！")
            self.returnHomepage()
        else:
            tk.messagebox.showerror(title="错误", message="用户权限修改失败！")

    def saveAccountInfo(self):
        #保存账户信息
        print("yes")
        newPassword=self.PasswordEntry.get()
        newEmail=self.emailEntry.get()
        if newPassword == "":
            tk.messagebox.showerror(title="错误", message="密码不能为空！")
            return

        result=update_User(self.cursor,self.UserID,newPassword,newEmail)

        if result:
            tk.messagebox.showinfo(title="成功", message="账户信息保存成功！")
            self.returnHomepage()
        else:
            tk.messagebox.showerror(title="错误", message="账户信息保存失败！")
            return




if __name__ == '__main__':
    # 登录界面，登陆成功后返回当前用户ID以及用户权限等级

    loginregister = LoginRegisterGui(cursor, connection)
    (CurrentUserID, UserLevel)=loginregister.get_User_info()
    print(CurrentUserID)
    print(UserLevel)

    #(CurrentUserID, UserLevel) = (1, 10000)

    # #测试用，直接进查询界面
    # querygui=queryGUI(cursor,connection,UserLevel)
    if CurrentUserID is not None or UserLevel is not None:
        mainGUI = MainGUI(cursor, connection, CurrentUserID, UserLevel)

