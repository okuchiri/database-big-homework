# -*- coding: utf-8 -*-
from datetime import datetime

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QRadioButton,
                               QSizePolicy, QStackedWidget, QTabWidget, QTableView,
                               QVBoxLayout, QWidget, QMessageBox, QStyledItemDelegate)
from DB_Management.query import *
from DB_Management.init_Cursor import *

# 全局cursor
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection

# 全局变量
user_id = -1
user_lvl = -1
ADMIN_LEVEL = 1000
search_result = []  # 搜索结果
current_document_id=-1 # 当前文档id


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.MainWidget = QTabWidget(Form)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setGeometry(QRect(0, 0, 800, 600))
        self.MainWidget.setStyleSheet(u"QTabBar::tab{width:90}\n"
                                      "QTabBar::tab{height:150}")
        self.MainWidget.setTabPosition(QTabWidget.TabPosition.East)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_main1 = QLabel(self.tab_4)
        self.label_main1.setObjectName(u"label_main1")
        self.label_main1.setGeometry(QRect(170, 170, 351, 81))
        self.label_main1.setStyleSheet(u"font: 9pt \"\u534e\u6587\u884c\u6977\";")
        self.pushButton_exit = QPushButton(self.tab_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(300, 470, 75, 23))
        self.label_name2 = QLabel(self.tab_4)
        self.label_name2.setObjectName(u"label_name2")
        self.label_name2.setGeometry(QRect(550, 470, 54, 16))
        self.label_name3 = QLabel(self.tab_4)
        self.label_name3.setObjectName(u"label_name3")
        self.label_name3.setGeometry(QRect(550, 490, 54, 16))
        self.label_name1 = QLabel(self.tab_4)
        self.label_name1.setObjectName(u"label_name1")
        self.label_name1.setGeometry(QRect(550, 450, 54, 16))
        self.label_name1_2 = QLabel(self.tab_4)
        self.label_name1_2.setObjectName(u"label_name1_2")
        self.label_name1_2.setGeometry(QRect(550, 510, 54, 16))
        self.MainWidget.addTab(self.tab_4, "")
        self.Logintab = QWidget()
        self.Logintab.setObjectName(u"Logintab")
        self.stackedWidget_3 = QStackedWidget(self.Logintab)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(20, 60, 501, 431))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_3.addWidget(self.page)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.layoutWidget = QWidget(self.page_login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 60, 341, 171))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_account_login = QLabel(self.layoutWidget)
        self.label_account_login.setObjectName(u"label_account_login")

        self.horizontalLayout_2.addWidget(self.label_account_login)

        self.lineEdit_account_login = QLineEdit(self.layoutWidget)
        self.lineEdit_account_login.setObjectName(u"lineEdit_account_login")

        self.horizontalLayout_2.addWidget(self.lineEdit_account_login)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_password_login = QLabel(self.layoutWidget)
        self.label_password_login.setObjectName(u"label_password_login")

        self.horizontalLayout_5.addWidget(self.label_password_login)

        self.lineEdit_password_login = QLineEdit(self.layoutWidget)
        self.lineEdit_password_login.setObjectName(u"lineEdit_password_login")

        self.horizontalLayout_5.addWidget(self.lineEdit_password_login)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.layoutWidget1 = QWidget(self.page_login)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 330, 261, 51))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yes_login = QPushButton(self.layoutWidget1)
        self.pushButton_yes_login.setObjectName(u"pushButton_yes_login")

        self.horizontalLayout_10.addWidget(self.pushButton_yes_login)

        self.stackedWidget_3.addWidget(self.page_login)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.layoutWidget_2 = QWidget(self.page_register)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(60, 60, 341, 171))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_account_register = QLabel(self.layoutWidget_2)
        self.label_account_register.setObjectName(u"label_account_register")

        self.horizontalLayout_7.addWidget(self.label_account_register)

        self.lineEdit_account_register = QLineEdit(self.layoutWidget_2)
        self.lineEdit_account_register.setObjectName(u"lineEdit_account_register")

        self.horizontalLayout_7.addWidget(self.lineEdit_account_register)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_password_register = QLabel(self.layoutWidget_2)
        self.label_password_register.setObjectName(u"label_password_register")

        self.horizontalLayout_9.addWidget(self.label_password_register)

        self.lineEdit_password_register = QLineEdit(self.layoutWidget_2)
        self.lineEdit_password_register.setObjectName(u"lineEdit_password_register")

        self.horizontalLayout_9.addWidget(self.lineEdit_password_register)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_password_2_register = QLabel(self.layoutWidget_2)
        self.label_password_2_register.setObjectName(u"label_password_2_register")

        self.horizontalLayout_14.addWidget(self.label_password_2_register)

        self.lineEdit_password_2_register = QLineEdit(self.layoutWidget_2)
        self.lineEdit_password_2_register.setObjectName(u"lineEdit_password_2_register")

        self.horizontalLayout_14.addWidget(self.lineEdit_password_2_register)

        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.layoutWidget_9 = QWidget(self.page_register)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(100, 330, 261, 51))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yes_register = QPushButton(self.layoutWidget_9)
        self.pushButton_yes_register.setObjectName(u"pushButton_yes_register")

        self.horizontalLayout_11.addWidget(self.pushButton_yes_register)

        self.pushButton_back_register = QPushButton(self.layoutWidget_9)
        self.pushButton_back_register.setObjectName(u"pushButton_back_register")

        self.horizontalLayout_11.addWidget(self.pushButton_back_register)

        self.stackedWidget_3.addWidget(self.page_register)
        self.page_adminspace = QWidget()
        self.page_adminspace.setObjectName(u"page_adminspace")
        self.layoutWidget_5 = QWidget(self.page_adminspace)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(60, 60, 341, 171))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_account_admin = QLabel(self.layoutWidget_5)
        self.label_account_admin.setObjectName(u"label_account_admin")

        self.horizontalLayout_8.addWidget(self.label_account_admin)

        self.lineEdit_account_admin = QLineEdit(self.layoutWidget_5)
        self.lineEdit_account_admin.setObjectName(u"lineEdit_account_admin")

        self.horizontalLayout_8.addWidget(self.lineEdit_account_admin)

        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_grade = QLabel(self.layoutWidget_5)
        self.label_grade.setObjectName(u"label_grade")

        self.horizontalLayout_13.addWidget(self.label_grade)

        self.lineEdit_grade = QLineEdit(self.layoutWidget_5)
        self.lineEdit_grade.setObjectName(u"lineEdit_grade")

        self.horizontalLayout_13.addWidget(self.lineEdit_grade)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.layoutWidget_10 = QWidget(self.page_adminspace)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(100, 330, 261, 51))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_rewrite = QPushButton(self.layoutWidget_10)
        self.pushButton_rewrite.setObjectName(u"pushButton_rewrite")

        self.horizontalLayout_12.addWidget(self.pushButton_rewrite)

        self.pushButton_back_admin = QPushButton(self.layoutWidget_10)
        self.pushButton_back_admin.setObjectName(u"pushButton_back_admin")

        self.horizontalLayout_12.addWidget(self.pushButton_back_admin)

        self.stackedWidget_3.addWidget(self.page_adminspace)
        self.page_userinfo = QWidget()
        self.page_userinfo.setObjectName(u"page_userinfo")
        self.layoutWidget_11 = QWidget(self.page_userinfo)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(100, 330, 261, 51))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_rewrite_user = QPushButton(self.layoutWidget_11)
        self.pushButton_rewrite_user.setObjectName(u"pushButton_rewrite_user")

        self.horizontalLayout_15.addWidget(self.pushButton_rewrite_user)

        self.pushButton_UserInfo_back = QPushButton(self.layoutWidget_11)
        self.pushButton_UserInfo_back.setObjectName(u"pushButton_UserInfo_back")

        self.horizontalLayout_15.addWidget(self.pushButton_UserInfo_back)

        self.layoutWidget_4 = QWidget(self.page_userinfo)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(60, 50, 381, 221))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_userid_user = QLabel(self.layoutWidget_4)
        self.label_userid_user.setObjectName(u"label_userid_user")

        self.horizontalLayout_25.addWidget(self.label_userid_user)

        self.lineEdit_userid_user = QLineEdit(self.layoutWidget_4)
        self.lineEdit_userid_user.setObjectName(u"lineEdit_userid_user")

        self.horizontalLayout_25.addWidget(self.lineEdit_userid_user)

        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_account_user = QLabel(self.layoutWidget_4)
        self.label_account_user.setObjectName(u"label_account_user")

        self.horizontalLayout_16.addWidget(self.label_account_user)

        self.lineEdit_account_user = QLineEdit(self.layoutWidget_4)
        self.lineEdit_account_user.setObjectName(u"lineEdit_account_user")

        self.horizontalLayout_16.addWidget(self.lineEdit_account_user)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_email_user = QLabel(self.layoutWidget_4)
        self.label_email_user.setObjectName(u"label_email_user")

        self.horizontalLayout_23.addWidget(self.label_email_user)

        self.lineEdit_email_user = QLineEdit(self.layoutWidget_4)
        self.lineEdit_email_user.setObjectName(u"lineEdit_email_user")

        self.horizontalLayout_23.addWidget(self.lineEdit_email_user)

        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_password_user = QLabel(self.layoutWidget_4)
        self.label_password_user.setObjectName(u"label_password_user")

        self.horizontalLayout_21.addWidget(self.label_password_user)

        self.lineEdit_password_user = QLineEdit(self.layoutWidget_4)
        self.lineEdit_password_user.setObjectName(u"lineEdit_password_user")

        self.horizontalLayout_21.addWidget(self.lineEdit_password_user)

        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_password_2_user = QLabel(self.layoutWidget_4)
        self.label_password_2_user.setObjectName(u"label_password_2_user")

        self.horizontalLayout_22.addWidget(self.label_password_2_user)

        self.lineEdit_password_2_user = QLineEdit(self.layoutWidget_4)
        self.lineEdit_password_2_user.setObjectName(u"lineEdit_password_2_user")

        self.horizontalLayout_22.addWidget(self.lineEdit_password_2_user)

        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.stackedWidget_3.addWidget(self.page_userinfo)
        self.layoutWidget2 = QWidget(self.Logintab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(530, 180, 101, 201))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_login = QPushButton(self.layoutWidget2)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.verticalLayout_12.addWidget(self.pushButton_login)

        self.pushButton_signin = QPushButton(self.layoutWidget2)
        self.pushButton_signin.setObjectName(u"pushButton_signin")

        self.verticalLayout_12.addWidget(self.pushButton_signin)

        self.pushButton_userinfo = QPushButton(self.layoutWidget2)
        self.pushButton_userinfo.setObjectName(u"pushButton_userinfo")

        self.verticalLayout_12.addWidget(self.pushButton_userinfo)

        self.pushButton_adminspace = QPushButton(self.layoutWidget2)
        self.pushButton_adminspace.setObjectName(u"pushButton_adminspace")

        self.verticalLayout_12.addWidget(self.pushButton_adminspace)

        self.MainWidget.addTab(self.Logintab, "")
        self.Searchtab = QWidget()
        self.Searchtab.setObjectName(u"Searchtab")
        self.stackedWidget = QStackedWidget(self.Searchtab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 60, 631, 521))
        self.page_querynull = QWidget()
        self.page_querynull.setObjectName(u"page_querynull")
        self.stackedWidget.addWidget(self.page_querynull)
        self.pagebasicsearch = QWidget()
        self.pagebasicsearch.setObjectName(u"pagebasicsearch")
        self.layoutWidget3 = QWidget(self.pagebasicsearch)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 611, 411))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_basicsearch = QComboBox(self.layoutWidget3)
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.setObjectName(u"comboBox_basicsearch")
        self.comboBox_basicsearch.setEnabled(True)
        self.comboBox_basicsearch.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_basicsearch)

        self.lineEdit_basicsearch = QLineEdit(self.layoutWidget3)
        self.lineEdit_basicsearch.setObjectName(u"lineEdit_basicsearch")
        self.lineEdit_basicsearch.setFrame(True)

        self.horizontalLayout.addWidget(self.lineEdit_basicsearch)

        self.pushButton_bs1 = QPushButton(self.layoutWidget3)
        self.pushButton_bs1.setObjectName(u"pushButton_bs1")

        self.horizontalLayout.addWidget(self.pushButton_bs1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableView_basicsearch = QTableView(self.layoutWidget3)
        self.tableView_basicsearch.setObjectName(u"tableView_basicsearch")

        self.verticalLayout_2.addWidget(self.tableView_basicsearch)

        self.stackedWidget.addWidget(self.pagebasicsearch)
        self.page_ShowDocInfo = QWidget()
        self.page_ShowDocInfo.setObjectName(u"page_ShowDocInfo")
        self.verticalLayoutWidget = QWidget(self.page_ShowDocInfo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 91, 421))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_title_front = QLabel(self.verticalLayoutWidget)
        self.label_title_front.setObjectName(u"label_title_front")

        self.verticalLayout_5.addWidget(self.label_title_front)

        self.label_author_front = QLabel(self.verticalLayoutWidget)
        self.label_author_front.setObjectName(u"label_author_front")

        self.verticalLayout_5.addWidget(self.label_author_front)

        self.label_keyword_front = QLabel(self.verticalLayoutWidget)
        self.label_keyword_front.setObjectName(u"label_keyword_front")

        self.verticalLayout_5.addWidget(self.label_keyword_front)

        self.label_src_front = QLabel(self.verticalLayoutWidget)
        self.label_src_front.setObjectName(u"label_src_front")

        self.verticalLayout_5.addWidget(self.label_src_front)

        self.label_tag_front = QLabel(self.verticalLayoutWidget)
        self.label_tag_front.setObjectName(u"label_tag_front")

        self.verticalLayout_5.addWidget(self.label_tag_front)

        self.label_journal_front = QLabel(self.verticalLayoutWidget)
        self.label_journal_front.setObjectName(u"label_journal_front")

        self.verticalLayout_5.addWidget(self.label_journal_front)

        self.label_jornalid = QLabel(self.verticalLayoutWidget)
        self.label_jornalid.setObjectName(u"label_jornalid")

        self.verticalLayout_5.addWidget(self.label_jornalid)

        self.label_page = QLabel(self.verticalLayoutWidget)
        self.label_page.setObjectName(u"label_page")

        self.verticalLayout_5.addWidget(self.label_page)

        self.verticalLayoutWidget_2 = QWidget(self.page_ShowDocInfo)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(110, 10, 511, 421))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_title_info = QLabel(self.verticalLayoutWidget_2)
        self.label_title_info.setObjectName(u"label_title_info")

        self.verticalLayout_9.addWidget(self.label_title_info)

        self.label_author_info = QLabel(self.verticalLayoutWidget_2)
        self.label_author_info.setObjectName(u"label_author_info")

        self.verticalLayout_9.addWidget(self.label_author_info)

        self.label_keyword_info = QLabel(self.verticalLayoutWidget_2)
        self.label_keyword_info.setObjectName(u"label_keyword_info")

        self.verticalLayout_9.addWidget(self.label_keyword_info)

        self.label_src_info = QLabel(self.verticalLayoutWidget_2)
        self.label_src_info.setObjectName(u"label_src_info")

        self.verticalLayout_9.addWidget(self.label_src_info)

        self.label_tag_info = QLabel(self.verticalLayoutWidget_2)
        self.label_tag_info.setObjectName(u"label_tag_info")

        self.verticalLayout_9.addWidget(self.label_tag_info)

        self.label_journal_info = QLabel(self.verticalLayoutWidget_2)
        self.label_journal_info.setObjectName(u"label_journal_info")

        self.verticalLayout_9.addWidget(self.label_journal_info)

        self.label_journalid_info = QLabel(self.verticalLayoutWidget_2)
        self.label_journalid_info.setObjectName(u"label_journalid_info")

        self.verticalLayout_9.addWidget(self.label_journalid_info)

        self.label_journalpage_info = QLabel(self.verticalLayoutWidget_2)
        self.label_journalpage_info.setObjectName(u"label_journalpage_info")

        self.verticalLayout_9.addWidget(self.label_journalpage_info)

        self.layoutWidget_3 = QWidget(self.page_ShowDocInfo)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(160, 450, 261, 51))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pushButton_edit = QPushButton(self.layoutWidget_3)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.horizontalLayout_24.addWidget(self.pushButton_edit)

        self.pushButton_backto_searchtab = QPushButton(self.layoutWidget_3)
        self.pushButton_backto_searchtab.setObjectName(u"pushButton_backto_searchtab")

        self.horizontalLayout_24.addWidget(self.pushButton_backto_searchtab)

        self.stackedWidget.addWidget(self.page_ShowDocInfo)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget_15 = QWidget(self.page_2)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(160, 450, 261, 51))
        self.horizontalLayout_26 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yes_insert_2 = QPushButton(self.layoutWidget_15)
        self.pushButton_yes_insert_2.setObjectName(u"pushButton_yes_insert_2")

        self.horizontalLayout_26.addWidget(self.pushButton_yes_insert_2)

        self.pushButton_empty_insert_2 = QPushButton(self.layoutWidget_15)
        self.pushButton_empty_insert_2.setObjectName(u"pushButton_empty_insert_2")

        self.horizontalLayout_26.addWidget(self.pushButton_empty_insert_2)

        self.pushButton_back_insert = QPushButton(self.layoutWidget_15)
        self.pushButton_back_insert.setObjectName(u"pushButton_back_insert")

        self.horizontalLayout_26.addWidget(self.pushButton_back_insert)

        self.layoutWidget_6 = QWidget(self.page_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 10, 611, 421))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_name_2 = QLabel(self.layoutWidget_6)
        self.label_name_2.setObjectName(u"label_name_2")

        self.verticalLayout_28.addWidget(self.label_name_2)

        self.lineEdit_name_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_name_2.setObjectName(u"lineEdit_name_2")

        self.verticalLayout_28.addWidget(self.lineEdit_name_2)

        self.horizontalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_gjc_2 = QLabel(self.layoutWidget_6)
        self.label_gjc_2.setObjectName(u"label_gjc_2")

        self.verticalLayout_29.addWidget(self.label_gjc_2)

        self.lineEdit_gjc_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_gjc_2.setObjectName(u"lineEdit_gjc_2")

        self.verticalLayout_29.addWidget(self.lineEdit_gjc_2)

        self.horizontalLayout_27.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_date_2 = QLabel(self.layoutWidget_6)
        self.label_date_2.setObjectName(u"label_date_2")

        self.verticalLayout_30.addWidget(self.label_date_2)

        self.lineEdit_date_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_date_2.setObjectName(u"lineEdit_date_2")

        self.verticalLayout_30.addWidget(self.lineEdit_date_2)

        self.horizontalLayout_27.addLayout(self.verticalLayout_30)

        self.verticalLayout_27.addLayout(self.horizontalLayout_27)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_author_2 = QLabel(self.layoutWidget_6)
        self.label_author_2.setObjectName(u"label_author_2")

        self.verticalLayout_32.addWidget(self.label_author_2)

        self.lineEdit_author_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_author_2.setObjectName(u"lineEdit_author_2")

        self.verticalLayout_32.addWidget(self.lineEdit_author_2)

        self.verticalLayout_31.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_author_4 = QLabel(self.layoutWidget_6)
        self.label_author_4.setObjectName(u"label_author_4")

        self.verticalLayout_33.addWidget(self.label_author_4)

        self.lineEdit_author_4 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_author_4.setObjectName(u"lineEdit_author_4")

        self.verticalLayout_33.addWidget(self.lineEdit_author_4)

        self.verticalLayout_31.addLayout(self.verticalLayout_33)

        self.verticalLayout_27.addLayout(self.verticalLayout_31)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_tag_2 = QLabel(self.layoutWidget_6)
        self.label_tag_2.setObjectName(u"label_tag_2")

        self.verticalLayout_34.addWidget(self.label_tag_2)

        self.lineEdit_tag_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_tag_2.setObjectName(u"lineEdit_tag_2")

        self.verticalLayout_34.addWidget(self.lineEdit_tag_2)

        self.horizontalLayout_28.addLayout(self.verticalLayout_34)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_src_2 = QLabel(self.layoutWidget_6)
        self.label_src_2.setObjectName(u"label_src_2")

        self.verticalLayout_35.addWidget(self.label_src_2)

        self.lineEdit_src_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_src_2.setObjectName(u"lineEdit_src_2")

        self.verticalLayout_35.addWidget(self.lineEdit_src_2)

        self.horizontalLayout_28.addLayout(self.verticalLayout_35)

        self.verticalLayout_27.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_journalname_2 = QLabel(self.layoutWidget_6)
        self.label_journalname_2.setObjectName(u"label_journalname_2")

        self.verticalLayout_36.addWidget(self.label_journalname_2)

        self.lineEdit_journalname_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_journalname_2.setObjectName(u"lineEdit_journalname_2")

        self.verticalLayout_36.addWidget(self.lineEdit_journalname_2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.labe_journalid_2 = QLabel(self.layoutWidget_6)
        self.labe_journalid_2.setObjectName(u"labe_journalid_2")

        self.verticalLayout_37.addWidget(self.labe_journalid_2)

        self.lineEdit_journalid_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_journalid_2.setObjectName(u"lineEdit_journalid_2")

        self.verticalLayout_37.addWidget(self.lineEdit_journalid_2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_journalpage_2 = QLabel(self.layoutWidget_6)
        self.label_journalpage_2.setObjectName(u"label_journalpage_2")

        self.verticalLayout_38.addWidget(self.label_journalpage_2)

        self.lineEdit_journalpage_2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_journalpage_2.setObjectName(u"lineEdit_journalpage_2")

        self.verticalLayout_38.addWidget(self.lineEdit_journalpage_2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_38)

        self.verticalLayout_27.addLayout(self.horizontalLayout_29)

        self.stackedWidget.addWidget(self.page_2)
        self.MainWidget.addTab(self.Searchtab, "")
        self.Insertiontab = QWidget()
        self.Insertiontab.setObjectName(u"Insertiontab")
        self.stackedWidget_2 = QStackedWidget(self.Insertiontab)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 60, 631, 521))
        self.page_analysisnull = QWidget()
        self.page_analysisnull.setObjectName(u"page_analysisnull")
        self.stackedWidget_2.addWidget(self.page_analysisnull)
        self.page_authoranalysis = QWidget()
        self.page_authoranalysis.setObjectName(u"page_authoranalysis")
        self.layoutWidget_14 = QWidget(self.page_authoranalysis)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(160, 450, 261, 51))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yes_insert = QPushButton(self.layoutWidget_14)
        self.pushButton_yes_insert.setObjectName(u"pushButton_yes_insert")

        self.horizontalLayout_20.addWidget(self.pushButton_yes_insert)

        self.pushButton_empty_insert = QPushButton(self.layoutWidget_14)
        self.pushButton_empty_insert.setObjectName(u"pushButton_empty_insert")

        self.horizontalLayout_20.addWidget(self.pushButton_empty_insert)

        self.layoutWidget4 = QWidget(self.page_authoranalysis)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 10, 611, 421))
        self.verticalLayout_26 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_name = QLabel(self.layoutWidget4)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_15.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget4)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_15.addWidget(self.lineEdit_name)

        self.horizontalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_gjc = QLabel(self.layoutWidget4)
        self.label_gjc.setObjectName(u"label_gjc")

        self.verticalLayout_16.addWidget(self.label_gjc)

        self.lineEdit_gjc = QLineEdit(self.layoutWidget4)
        self.lineEdit_gjc.setObjectName(u"lineEdit_gjc")

        self.verticalLayout_16.addWidget(self.lineEdit_gjc)

        self.horizontalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_date = QLabel(self.layoutWidget4)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_17.addWidget(self.label_date)

        self.lineEdit_date = QLineEdit(self.layoutWidget4)
        self.lineEdit_date.setObjectName(u"lineEdit_date")

        self.verticalLayout_17.addWidget(self.lineEdit_date)

        self.horizontalLayout_17.addLayout(self.verticalLayout_17)

        self.verticalLayout_26.addLayout(self.horizontalLayout_17)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_author = QLabel(self.layoutWidget4)
        self.label_author.setObjectName(u"label_author")

        self.verticalLayout_18.addWidget(self.label_author)

        self.lineEdit_author = QLineEdit(self.layoutWidget4)
        self.lineEdit_author.setObjectName(u"lineEdit_author")

        self.verticalLayout_18.addWidget(self.lineEdit_author)

        self.verticalLayout_25.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_author_3 = QLabel(self.layoutWidget4)
        self.label_author_3.setObjectName(u"label_author_3")

        self.verticalLayout_19.addWidget(self.label_author_3)

        self.lineEdit_author_3 = QLineEdit(self.layoutWidget4)
        self.lineEdit_author_3.setObjectName(u"lineEdit_author_3")

        self.verticalLayout_19.addWidget(self.lineEdit_author_3)

        self.verticalLayout_25.addLayout(self.verticalLayout_19)

        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_tag = QLabel(self.layoutWidget4)
        self.label_tag.setObjectName(u"label_tag")

        self.verticalLayout_20.addWidget(self.label_tag)

        self.lineEdit_tag = QLineEdit(self.layoutWidget4)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")

        self.verticalLayout_20.addWidget(self.lineEdit_tag)

        self.horizontalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_src = QLabel(self.layoutWidget4)
        self.label_src.setObjectName(u"label_src")

        self.verticalLayout_21.addWidget(self.label_src)

        self.lineEdit_src = QLineEdit(self.layoutWidget4)
        self.lineEdit_src.setObjectName(u"lineEdit_src")

        self.verticalLayout_21.addWidget(self.lineEdit_src)

        self.horizontalLayout_19.addLayout(self.verticalLayout_21)

        self.verticalLayout_26.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_journalname = QLabel(self.layoutWidget4)
        self.label_journalname.setObjectName(u"label_journalname")

        self.verticalLayout_22.addWidget(self.label_journalname)

        self.lineEdit_journalname = QLineEdit(self.layoutWidget4)
        self.lineEdit_journalname.setObjectName(u"lineEdit_journalname")

        self.verticalLayout_22.addWidget(self.lineEdit_journalname)

        self.horizontalLayout_18.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labe_journalid = QLabel(self.layoutWidget4)
        self.labe_journalid.setObjectName(u"labe_journalid")

        self.verticalLayout_23.addWidget(self.labe_journalid)

        self.lineEdit_journalid = QLineEdit(self.layoutWidget4)
        self.lineEdit_journalid.setObjectName(u"lineEdit_journalid")

        self.verticalLayout_23.addWidget(self.lineEdit_journalid)

        self.horizontalLayout_18.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_journalpage = QLabel(self.layoutWidget4)
        self.label_journalpage.setObjectName(u"label_journalpage")

        self.verticalLayout_24.addWidget(self.label_journalpage)

        self.lineEdit_journalpage = QLineEdit(self.layoutWidget4)
        self.lineEdit_journalpage.setObjectName(u"lineEdit_journalpage")

        self.verticalLayout_24.addWidget(self.lineEdit_journalpage)

        self.horizontalLayout_18.addLayout(self.verticalLayout_24)

        self.verticalLayout_26.addLayout(self.horizontalLayout_18)

        self.stackedWidget_2.addWidget(self.page_authoranalysis)
        self.MainWidget.addTab(self.Insertiontab, "")

        self.retranslateUi(Form)

        # 初页面设置
        self.MainWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.comboBox_basicsearch.setCurrentIndex(-1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.pushButton_userinfo.setVisible(False)
        self.pushButton_UserInfo_back.setVisible(False)
        self.pushButton_login.setVisible(False)
        self.pushButton_adminspace.setVisible(False)
        self.MainWidget.setTabEnabled(2, False)
        self.MainWidget.setTabEnabled(3, False)
        currentdatetime=datetime.now()
        formatted_date=currentdatetime.strftime("%Y-%m-%d")
        self.lineEdit_date.setText(formatted_date)


        QMetaObject.connectSlotsByName(Form)
        '-------------------------------槽函数连接处-------------------------------'
        self.pushButton_exit.clicked.connect(Form.close)
        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)
        self.pushButton_signin.clicked.connect(self.on_pushButton_register_clicked)
        self.pushButton_adminspace.clicked.connect(self.on_pushButton_admin_clicked)
        self.pushButton_yes_register.clicked.connect(self.on_pushButton_yes_register_clicked)
        self.pushButton_back_register.clicked.connect(self.on_pushButton_back_register_clicked)
        self.pushButton_bs1.clicked.connect(self.on_pushButton_bs1_clicked)
        self.pushButton_yes_insert.clicked.connect(self.on_pushButton_yes_insert_clicked)
        self.pushButton_yes_login.clicked.connect(self.on_pushBotton_yes_login_clicked)
        self.pushButton_rewrite.clicked.connect(self.on_pushButton_rewrite_clicked)
        self.pushButton_back_admin.clicked.connect(self.on_pushButton_back_admin_clicked)
        self.pushButton_userinfo.clicked.connect(self.on_pushButton_userinfo_clicked)
        self.pushButton_UserInfo_back.clicked.connect(self.on_pushButton_UserInfo_back_clicked)
        self.pushButton_rewrite_user.clicked.connect(self.on_pushButton_rewrite_user_clicked)
        self.tableView_basicsearch.doubleClicked.connect(self.on_tableView_basicsearch_doubleClicked)
        self.pushButton_backto_searchtab.clicked.connect(self.on_pushButton_backto_searchtab_clicked)
        self.pushButton_back_insert.clicked.connect(self.on_pushButton_back_insert_clicked)
        self.pushButton_edit.clicked.connect(self.on_pushButton_edit_clicked)
        self.pushButton_yes_insert_2.clicked.connect(self.on_pushButton_yes_insert_2_clicked)
        self.pushButton_empty_insert.clicked.connect(self.on_pushButton_empty_insert_clicked)
        self.pushButton_empty_insert_2.clicked.connect(self.on_pushButton_empty_insert_clicked_2)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_main1.setText(QCoreApplication.translate("Form",
                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">\u79d1\u5b66\u6587\u732e\u7ba1\u7406\u7cfb\u7edf</span></p></body></html>",
                                                            None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label_name2.setText(QCoreApplication.translate("Form", u"\u90b5\u5f08", None))
        self.label_name3.setText(QCoreApplication.translate("Form", u"\u6f58\u6cfd\u8f69", None))
        self.label_name1.setText(QCoreApplication.translate("Form", u"\u674e\u704f\u7199", None))
        self.label_name1_2.setText(QCoreApplication.translate("Form", u"\u9648\u4fca\u5c79", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab_4),
                                   QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.label_account_login.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\uff1a", None))
        self.lineEdit_account_login.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d\u6216\u90ae\u7bb1", None))
        self.label_password_login.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a", None))
        self.lineEdit_password_login.setText("")
        self.pushButton_yes_login.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u767b\u5f55", None))
        self.label_account_register.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a   ", None))
        self.label_password_register.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a      ", None))
        self.lineEdit_password_register.setText("")
        self.label_password_2_register.setText(
            QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.lineEdit_password_2_register.setText("")
        self.pushButton_yes_register.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u6ce8\u518c", None))
        self.pushButton_back_register.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_account_admin.setText(
            QCoreApplication.translate("Form", u"\u9700\u8981\u4fee\u6539\u7684\u7528\u6237\uff1a", None))
        self.label_grade.setText(
            QCoreApplication.translate("Form", u"\u65b0\u7684\u6743\u9650\u7b49\u7ea7\uff1a   ", None))
        self.lineEdit_grade.setText("")
        self.pushButton_rewrite.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u4fee\u6539", None))
        self.pushButton_back_admin.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.pushButton_rewrite_user.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u4fee\u6539", None))
        self.pushButton_UserInfo_back.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_userid_user.setText(QCoreApplication.translate("Form", u"\u7528\u6237ID\uff1a   ", None))
        self.label_account_user.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a   ", None))
        self.label_email_user.setText(QCoreApplication.translate("Form", u"\u90ae\u7bb1\uff1a      ", None))
        self.label_password_user.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a      ", None))
        self.lineEdit_password_user.setText("")
        self.label_password_2_user.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.lineEdit_password_2_user.setText("")
        self.pushButton_login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_signin.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.pushButton_userinfo.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u4fe1\u606f", None))
        self.pushButton_adminspace.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u754c\u9762", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Logintab),
                                   QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.comboBox_basicsearch.setItemText(0, QCoreApplication.translate("Form", u"\u4f5c\u8005", None))
        self.comboBox_basicsearch.setItemText(1, QCoreApplication.translate("Form", u"\u8bba\u6587", None))
        self.comboBox_basicsearch.setItemText(2, QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd", None))
        self.comboBox_basicsearch.setItemText(3, QCoreApplication.translate("Form", u"\u671f\u520a", None))

        self.comboBox_basicsearch.setCurrentText("")
        self.lineEdit_basicsearch.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5b8c\u6574\u67e5\u8be2\u5185\u5bb9", None))
        self.pushButton_bs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.label_title_front.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
        self.label_author_front.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005", None))
        self.label_keyword_front.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd", None))
        self.label_src_front.setText(QCoreApplication.translate("Form", u"\u6765\u6e90", None))
        self.label_tag_front.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.label_journal_front.setText(QCoreApplication.translate("Form", u"\u671f\u520a", None))
        self.label_jornalid.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u53f7", None))
        self.label_page.setText(QCoreApplication.translate("Form", u"\u9875\u7801", None))
        self.label_title_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_author_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_keyword_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_src_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_tag_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_journal_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_journalid_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_journalpage_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_edit.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91\u6587\u732e\u4fe1\u606f", None))
        self.pushButton_backto_searchtab.setText(QCoreApplication.translate("Form", u" \u8fd4\u56de", None))
        self.pushButton_yes_insert_2.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.pushButton_empty_insert_2.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.pushButton_back_insert.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_name_2.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u540d\u79f0\uff1a", None))
        self.label_gjc_2.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\uff1a", None))
        self.label_date_2.setText(
            QCoreApplication.translate("Form", u"\u53d1\u8868\u65e5\u671f\uff08yy-MM-dd\uff09\uff1a", None))
        self.label_author_2.setText(QCoreApplication.translate("Form",
                                                               u"\u6587\u6863\u7b2c\u4e00\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                               None))
        self.label_author_4.setText(QCoreApplication.translate("Form",
                                                               u"\u6587\u6863\u7b2c\u4e8c\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                               None))
        self.label_tag_2.setText(QCoreApplication.translate("Form",
                                                            u"\u6587\u6863\u6807\u7b7e\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                            None))
        self.label_src_2.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u6765\u6e90\uff1a", None))
        self.label_journalname_2.setText(
            QCoreApplication.translate("Form", u"\u6587\u6863\u671f\u520a\u540d\u79f0\uff1a", None))
        self.labe_journalid_2.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u671f\u53f7\uff1a", None))
        self.label_journalpage_2.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u9875\u6570\uff1a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Searchtab),
                                   QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.pushButton_yes_insert.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.pushButton_empty_insert.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u540d\u79f0\uff1a", None))
        self.label_gjc.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\uff1a", None))
        self.label_date.setText(
            QCoreApplication.translate("Form", u"\u53d1\u8868\u65e5\u671f\uff08yy-MM-dd\uff09\uff1a", None))
        self.label_author.setText(QCoreApplication.translate("Form",
                                                             u"\u6587\u6863\u7b2c\u4e00\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                             None))
        self.label_author_3.setText(QCoreApplication.translate("Form",
                                                               u"\u6587\u6863\u7b2c\u4e8c\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                               None))
        self.label_tag.setText(QCoreApplication.translate("Form",
                                                          u"\u6587\u6863\u6807\u7b7e\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a",
                                                          None))
        self.label_src.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u6765\u6e90\uff1a", None))
        self.label_journalname.setText(
            QCoreApplication.translate("Form", u"\u6587\u6863\u671f\u520a\u540d\u79f0\uff1a", None))
        self.labe_journalid.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u671f\u53f7\uff1a", None))
        self.label_journalpage.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u9875\u6570\uff1a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Insertiontab),
                                   QCoreApplication.translate("Form", u"\u63d2\u5165", None))

    # retranslateUi

    '--------------------------函数处--------------------------------'

    def display_data(self, table_view, data_list, headers):
        # 创建 QStandardItemModel
        model = QStandardItemModel()

        # 设置表头
        model.setHorizontalHeaderLabels(headers)

        # 填充数据
        for row in data_list:
            items = []
            for cell in row:
                item = QStandardItem(str(cell))
                # 设置文本居中
                item.setTextAlignment(Qt.AlignCenter)
                items.append(item)
            model.appendRow(items)

        # 设置模型到指定 QTableView
        table_view.setModel(model)

    # 按钮一：打开第一个面板
    def on_pushButton_login_clicked(self):
        global user_id, user_lvl
        if user_lvl != -1:
            QMessageBox.warning(self.page_login, "Warning", "您已完成登录")
            return
        #self.pushButton_back_login.setVisible(False)
        self.stackedWidget_3.setCurrentIndex(1)

    def on_pushButton_register_clicked(self):
        global user_id, user_lvl
        if user_lvl != -1:
            QMessageBox.warning(self.page_login, "Warning", "您已完成登录")
            return
        self.pushButton_login.setVisible(False)  # 禁用登录按钮
        self.pushButton_signin.setVisible(False)
        self.stackedWidget_3.setCurrentIndex(2)

    def on_pushButton_yes_register_clicked(self):
        global user_id, user_lvl
        if user_lvl != -1:
            QMessageBox.warning(self.page_login, "Warning", "您已完成登录")
            return
        username = self.lineEdit_account_register.text()
        password = self.lineEdit_password_register.text()
        password2 = self.lineEdit_password_2_register.text()
        if username == "" or password == "":
            QMessageBox.warning(self.page_register, "Warning", "用户名或密码不能为空！")
            return
        if password != password2:
            QMessageBox.warning(self.page_register, "Warning", "两次输入的密码不一致！")
            return

        (result, userid) = new_User(cursor, username, password)
        if result:
            QMessageBox.information(self.page_register, "Information", "注册成功！请登录")
            # user_id = userid
            # user_lvl = 1
            self.stackedWidget_3.setCurrentIndex(1)
            # self.pushButton_login.setVisible(True)
        else:
            QMessageBox.warning(self.page_register, "Warning", "用户名已存在！")
            return

    def on_pushBotton_yes_login_clicked(self):
        global user_id, user_lvl
        if user_lvl != -1:
            QMessageBox.warning(self.page_login, "Warning", "您已完成登录")
            return
        #self.pushButton_login.setVisible(True)
        username = self.lineEdit_account_login.text()
        email = self.lineEdit_account_login.text()
        password = self.lineEdit_password_login.text()
        if username == "" or password == "":
            QMessageBox.warning(self.page_login, "Warning", "用户名或密码不能为空！")
            return

        (result, userid, permission) = login_query(cursor, username, password)
        if result:
            QMessageBox.information(self.page_login, "Information", "登录成功！")
            user_id = userid
            user_lvl = permission
            self.MainWidget.setTabEnabled(2, True)
            self.MainWidget.setTabEnabled(3, True)
            self.pushButton_userinfo.setVisible(True)
            self.pushButton_adminspace.setVisible(True)
            self.pushButton_signin.setVisible(False)
            self.on_pushButton_userinfo_clicked()
        else:
            (result, userid, permission) = login_query_email(cursor, email, password)
            if result:
                QMessageBox.information(self.page_login, "Information", "登录成功！")
                user_id = userid
                user_lvl = permission
                self.MainWidget.setTabEnabled(2, True)
                self.MainWidget.setTabEnabled(3, True)
                self.pushButton_userinfo.setVisible(True)
                self.pushButton_adminspace.setVisible(True)
                self.pushButton_signin.setVisible(False)
                self.on_pushButton_userinfo_clicked()
            else:
                QMessageBox.warning(self.page_login, "Warning", "用户名或密码错误！")

    def on_pushButton_back_register_clicked(self):
        self.stackedWidget_3.setCurrentIndex(1)
        self.pushButton_signin.setVisible(True)

    def on_pushButton_admin_clicked(self):
        if user_lvl < ADMIN_LEVEL:
            QMessageBox.warning(self.page_login, "Warning", "非管理员禁止访问！")
            return
        self.stackedWidget_3.setCurrentIndex(3)

    def on_basicsearch_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_pushButton_bs1_clicked(self):
        content = self.lineEdit_basicsearch.text()
        choice = self.comboBox_basicsearch.currentIndex()
        print(choice)
        global search_result
        search_result = []
        if choice == -1 or choice == 1:
            search_result = query_with_title(cursor, content)
            if search_result == []:
                QMessageBox.warning(self.pagebasicsearch, "Warning", "未找到相关内容！")
            else:
                self.tableView_basicsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_basicsearch.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                filtered_data = [[row[1], row[2]] for row in search_result]
                self.display_data(self.tableView_basicsearch, filtered_data, ["文档名称", "文档来源"])
        elif choice == 0:
            search_result = query_with_authorname(cursor, content)
            if search_result == []:
                QMessageBox.warning(self.pagebasicsearch, "Warning", "未找到相关内容！")
            else:
                self.tableView_basicsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_basicsearch.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                filtered_data = [[row[1], row[2]] for row in search_result]
                self.display_data(self.tableView_basicsearch, filtered_data, ["文档名称", "作者"])
        elif choice == 2:  # 还没写关键词检索
            search_result = "暂未开通"
        elif choice == 3:
            search_result = query_with_journalname(cursor, content)
            if search_result == []:
                QMessageBox.warning(self.pagebasicsearch, "Warning", "未找到相关内容！")
            else:
                self.tableView_basicsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_basicsearch.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                filtered_data = [[row[1], row[2]] for row in search_result]
                self.display_data(self.tableView_basicsearch, filtered_data, ["文档名称", "期刊名称"])
        elif choice == 4:
            search_result = query_with_tag(cursor, content)
            if search_result == []:
                QMessageBox.warning(self.pagebasicsearch, "Warning", "未找到相关内容！")
            else:
                self.tableView_basicsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_basicsearch.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                filtered_data = [[row[1], row[2]] for row in search_result]
                self.display_data(self.tableView_basicsearch, filtered_data, ["文档名称", "标签"])

    def on_pushButton_yes_insert_clicked(self):
        title = self.lineEdit_name.text()
        author1 = self.lineEdit_author.text()
        author2 = self.lineEdit_author_3.text()
        tag = self.lineEdit_tag.text()
        src = self.lineEdit_src.text()
        journalname = self.lineEdit_journalname.text()
        journalissue = self.lineEdit_journalid.text()
        journalpage = self.lineEdit_journalpage.text()
        keyword = self.lineEdit_gjc.text()
        date = self.lineEdit_date.text()
        # 检测输入是否为空
        if title == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "标题不能为空！")
            return
        if author1 == "" and author2 == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "作者不能为空！")
            return
        if tag == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "标签不能为空！")
            return
        if journalname == "":
            journalname = "None"
        if journalissue == "":
            journalissue = -1
        if journalpage == "":
            journalpage = -1
        if src == "":
            src = "None"

        authorlist01 = author1.split(",")
        authorlist02 = author2.split(",")
        taglist = tag.split(",")
        authoridlist01 = []
        authoridlist02 = []
        tagidlist = []

        # 检测作者表中是否存在该作者，不存在则插入
        for author in authorlist01:
            if author == "":
                continue
            (res, id) = query_author_id(cursor, author)
            if res == False:
                authoridlist01.append(new_Author(cursor, author))
            else:
                authoridlist01.append(id)
        for author in authorlist02:
            if author == "":
                continue
            (res, id) = query_author_id(cursor, author)
            if res == False:
                authoridlist02.append(new_Author(cursor, author))
            else:
                authoridlist02.append(id)

        # 检测标签表中是否存在该标签，不存在则插入
        for tag in taglist:
            if tag == "":
                continue
            (res, id) = query_tag_id(cursor, tag)
            if res == False:
                tagidlist.append(new_Tag(cursor, tag))
            else:
                tagidlist.append(id)

        # journalid
        journalid = -1;
        (res, id) = query_journal_id(cursor, journalname)
        if not res:
            journalid = new_Journal(cursor, journalname)
        print(journalid)

        # 新建文档
        documentid = new_Document(cursor, title, date, src, keyword);
        print(documentid)
        documentid = int(documentid)

        # 插入作者信息
        for authorid in authoridlist01:
            if authorid == "":
                continue
            print(type(authorid))
            new_DocumentAuthor(cursor, documentid, authorid, 1)
        for authorid in authoridlist02:
            if authorid == "":
                continue
            new_DocumentAuthor(cursor, documentid, authorid, 2)
        # 插入标签信息
        for tagid in tagidlist:
            if authorid == "":
                continue
            new_DocumentTag(cursor, documentid, tagid)
        # 插入期刊信息
        new_JournalPos(cursor, documentid, journalid, journalissue, journalpage)
        QMessageBox.information(self.page_authoranalysis, "Information", "插入成功！")

    def on_pushButton_rewrite_user_clicked(self):
        username = self.lineEdit_account_user.text()
        new_password = self.lineEdit_password_user.text()
        new_password2 = self.lineEdit_password_2_user.text()
        new_email = self.lineEdit_email_user.text()
        if username == "" or new_password == "":
            QMessageBox.warning(self.page_register, "Warning", "用户名或密码不能为空！")
            return
        if new_password != new_password2:
            QMessageBox.warning(self.page_register, "Warning", "两次密码不一致！")
            return
        if new_email != "" and new_email != None:
            flag = check_email(cursor, new_email)
            if flag == False:
                QMessageBox.warning(self.page_register, "Warning", "该邮箱已被注册！")
                return
        result = update_User(cursor, username, user_id, new_password, new_email)
        if result:
            QMessageBox.information(self.page_authoranalysis, "Information", "成功修改个人信息！")
        else:
            QMessageBox.warning(self.page_register, "Warning", "用户名已存在")

    def on_pushButton_rewrite_clicked(self):
        aim_userid = self.lineEdit_account_admin.text()
        aim_lvl = ""
        try:
            aim_lvl = int(self.lineEdit_grade.text())
        except ValueError:
            aim_lvl = 1
            QMessageBox.warning(self.page_adminspace, "Warning", "请输入数字！")
            self.lineEdit_grade.settext(str(aim_lvl))
            return
        if aim_userid == "":
            QMessageBox.warning(self.page_adminspace, "Warning", "用户名不能为空！")
            return

        (resulttmp, userinfo) = query_all_Userinfo(cursor, aim_userid)
        if resulttmp == False:
            QMessageBox.warning(self.page_adminspace, "Warning", "用户不存在！")
            return

        result = update_User_permission(cursor, aim_userid, aim_lvl)
        if result == True:
            QMessageBox.information(self.page_adminspace, "Information", "修改成功！")
        else:
            QMessageBox.warning(self.page_adminspace, "Warning", "修改失败！")
        return

    def on_pushButton_back_admin_clicked(self):
        self.stackedWidget_3.setCurrentIndex(4)

    def on_pushButton_userinfo_clicked(self):
        self.stackedWidget_3.setCurrentIndex(4)
        # 显示用户信息
        (result, userinfo) = query_all_Userinfo(cursor, user_id)
        if result == False:
            QMessageBox.warning(self.page_userinfo, "Warning", "用户不存在！")
            return
        self.lineEdit_userid_user.setText(str(userinfo[0]))
        self.lineEdit_account_user.setText(str(userinfo[1]))
        self.lineEdit_email_user.setText(str(userinfo[2]))

    def on_pushButton_UserInfo_back_clicked(self):
        self.stackedWidget_3.setCurrentIndex(1)

    def on_tableView_basicsearch_doubleClicked(self):
        self.pushButton_backto_searchtab.setVisible(True)
        global search_result
        global current_document_id
        row = self.tableView_basicsearch.currentIndex().row()
        document_id = search_result[row][0]  # 得到文档id
        current_document_id=document_id
        print(document_id)
        self.stackedWidget.setCurrentIndex(2)

        # 获取文档信息
        (DocInfo, AuthorInfo, TagInfo, JournalInfo) = query_all_with_documentid(cursor, document_id)
        Doctitle = DocInfo[1]
        self.label_title_info.setText(Doctitle)

        keyword = DocInfo[4]
        if keyword == "":
            keyword = "None"
        self.label_keyword_info.setText(keyword)

        src = DocInfo[3]
        if src == "":
            src = "None"
        self.label_src_info.setText(src)

        tag = ""
        for i in range(len(TagInfo)):
            tag += TagInfo[i][1] + " "
        if tag == "":
            tag = "None"
        self.label_tag_info.setText(tag)

        author1 = ""
        author2 = ""
        for i in range(len(AuthorInfo)):
            if AuthorInfo[i][2] == 1:
                author1 += AuthorInfo[i][1] + " "
            else:
                author2 += AuthorInfo[i][1] + " "
        if author1 == "":
            author1 = "None"
        if author2 == "":
            author2 = "None"
        author = "第一作者:" + author1 + " 第二作者:" + author2
        self.label_author_info.setText(author)

        if JournalInfo == None:
            self.label_journal_info.setText("None")
            return

        print(JournalInfo)
        journallabel = ""
        if JournalInfo[1] == "":
            journallabel += "None"
        else:
            journallabel += JournalInfo[1]
        self.label_journal_info.setText(journallabel)
        journallabel = ""
        if JournalInfo[2] == -1:
            journallabel += "None"
        else:
            journallabel += str(JournalInfo[2])
        self.label_journalid_info.setText(journallabel)
        journallabel += ""
        if JournalInfo[3] == "":
            journallabel += "None"
        else:
            journallabel = str(JournalInfo[3])
        self.label_journalpage_info.setText(journallabel)

    def on_pushButton_backto_searchtab_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_pushButton_back_insert_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_pushButton_edit_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        global current_document_id
        # 获取文档信息
        (DocInfo, AuthorInfo, TagInfo, JournalInfo) = query_all_with_documentid(cursor, current_document_id)
        # 显示文档信息
        self.lineEdit_name_2.setText(DocInfo[1])
        keyword = DocInfo[4]
        self.lineEdit_gjc_2.setText(keyword)

        src = DocInfo[3]
        self.lineEdit_src_2.setText(src)

        date=str(DocInfo[2])
        self.lineEdit_date_2.setText(date)

        tag = ""
        for i in range(len(TagInfo)):
            tag += TagInfo[i][1] + ","
        tag=tag.rstrip(",")
        self.lineEdit_tag_2.setText(tag)

        author1 = ""
        author2 = ""
        for i in range(len(AuthorInfo)):
            if AuthorInfo[i][2] == 1:
                author1 += AuthorInfo[i][1] + ","
            else:
                author2 += AuthorInfo[i][1] + ","
        author1=author1.rstrip(",")
        author2=author2.rstrip(",")
        self.lineEdit_author_2.setText(author1)
        self.lineEdit_author_4.setText(author2)

        if JournalInfo == None:
            return
        else:
            self.lineEdit_journalname_2.setText(JournalInfo[1])
            self.lineEdit_journalid_2.setText(str(JournalInfo[2]))
            self.lineEdit_journalpage_2.setText(str(JournalInfo[3]))


    def on_pushButton_yes_insert_2_clicked(self):
        print("yes_insert_2")
        global current_document_id
        title = self.lineEdit_name_2.text()
        author1 = self.lineEdit_author_2.text()
        author2 = self.lineEdit_author_4.text()
        tag = self.lineEdit_tag_2.text()
        src = self.lineEdit_src_2.text()
        journalname = self.lineEdit_journalname_2.text()
        journalissue = self.lineEdit_journalid_2.text()
        journalpage = self.lineEdit_journalpage_2.text()
        keyword = self.lineEdit_gjc_2.text()
        date = self.lineEdit_date_2.text()
        # 检测输入是否为空
        if title == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "标题不能为空！")
            return
        if author1 == "" and author2 == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "作者不能为空！")
            return
        if tag == "":
            QMessageBox.warning(self.page_authoranalysis, "Warning", "标签不能为空！")
            return

        #还没写完


    def on_pushButton_empty_insert_clicked(self):
        self.lineEdit_name.clear()
        self.lineEdit_author.clear()
        self.lineEdit_author_3.clear()
        self.lineEdit_tag.clear()
        self.lineEdit_src.clear()
        self.lineEdit_journalname.clear()
        self.lineEdit_journalid.clear()
        self.lineEdit_journalpage.clear()
        self.lineEdit_gjc.clear()


    def on_pushButton_empty_insert_clicked_2(self):
        self.lineEdit_name_2.clear()
        self.lineEdit_author_2.clear()
        self.lineEdit_author_4.clear()
        self.lineEdit_tag_2.clear()
        self.lineEdit_src_2.clear()
        self.lineEdit_journalname_2.clear()
        self.lineEdit_journalid_2.clear()
        self.lineEdit_journalpage_2.clear()
        self.lineEdit_gjc_2.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    with open("style.qss", encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    Form.show()
    sys.exit(app.exec())
