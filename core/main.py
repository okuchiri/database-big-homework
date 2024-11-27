from LoginGUI import LoginRegisterGui
from DB_Management.init_Cursor import init_Cursor

# 连接数据库,获取游标
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection



#登录界面，登陆成功后返回当前用户ID以及用户权限等级
loginregister = LoginRegisterGui(cursor, connection)
(CurrentUserID, UserLevel)=loginregister.get_User_info()
print(CurrentUserID)
print(UserLevel)

