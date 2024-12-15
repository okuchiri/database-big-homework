# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QRadioButton,
                               QSizePolicy, QStackedWidget, QTabWidget, QTableView,
                               QVBoxLayout, QWidget, QMessageBox)

from DB_Management.query import *
from DB_Management.init_Cursor import *

#全局cursor
DBCONNECTOR = init_Cursor()
cursor = DBCONNECTOR.cursor
connection = DBCONNECTOR.connection

#全局变量
user_id=-1
user_lvl=-1
ADMIN_LEVEL=1000


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
        self.MainWidget.setTabPosition(QTabWidget.East)
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

        self.pushButton_back_login = QPushButton(self.layoutWidget1)
        self.pushButton_back_login.setObjectName(u"pushButton_back_login")

        self.horizontalLayout_10.addWidget(self.pushButton_back_login)

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
        self.page_particalsearch_2 = QWidget()
        self.page_particalsearch_2.setObjectName(u"page_particalsearch_2")
        self.layoutWidget_5 = QWidget(self.page_particalsearch_2)
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

        self.layoutWidget_10 = QWidget(self.page_particalsearch_2)
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

        self.stackedWidget_3.addWidget(self.page_particalsearch_2)
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

        self.pushButton_adminspace = QPushButton(self.layoutWidget2)
        self.pushButton_adminspace.setObjectName(u"pushButton_adminspace")

        self.verticalLayout_12.addWidget(self.pushButton_adminspace)

        self.MainWidget.addTab(self.Logintab, "")
        self.Searchtab = QWidget()
        self.Searchtab.setObjectName(u"Searchtab")
        self.stackedWidget = QStackedWidget(self.Searchtab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 60, 501, 431))
        self.page_querynull = QWidget()
        self.page_querynull.setObjectName(u"page_querynull")
        self.stackedWidget.addWidget(self.page_querynull)
        self.pagebasicsearch = QWidget()
        self.pagebasicsearch.setObjectName(u"pagebasicsearch")
        self.layoutWidget3 = QWidget(self.pagebasicsearch)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 50, 491, 311))
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
        self.page_particalsearch = QWidget()
        self.page_particalsearch.setObjectName(u"page_particalsearch")
        self.layoutWidget_3 = QWidget(self.page_particalsearch)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 50, 491, 311))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_particalsearch = QRadioButton(self.layoutWidget_3)
        self.radioButton_particalsearch.setObjectName(u"radioButton_particalsearch")

        self.horizontalLayout_3.addWidget(self.radioButton_particalsearch)

        self.lineEdit_particalsearch = QLineEdit(self.layoutWidget_3)
        self.lineEdit_particalsearch.setObjectName(u"lineEdit_particalsearch")

        self.horizontalLayout_3.addWidget(self.lineEdit_particalsearch)

        self.pushButton_ps1 = QPushButton(self.layoutWidget_3)
        self.pushButton_ps1.setObjectName(u"pushButton_ps1")

        self.horizontalLayout_3.addWidget(self.pushButton_ps1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tableView_particalsearch = QTableView(self.layoutWidget_3)
        self.tableView_particalsearch.setObjectName(u"tableView_particalsearch")

        self.verticalLayout_4.addWidget(self.tableView_particalsearch)

        self.stackedWidget.addWidget(self.page_particalsearch)
        self.layoutWidget4 = QWidget(self.Searchtab)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(530, 230, 101, 103))
        self.verticalLayout = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_basicsearch = QPushButton(self.layoutWidget4)
        self.pushButton_basicsearch.setObjectName(u"pushButton_basicsearch")

        self.verticalLayout.addWidget(self.pushButton_basicsearch)

        self.pushButton_particalsearch = QPushButton(self.layoutWidget4)
        self.pushButton_particalsearch.setObjectName(u"pushButton_particalsearch")

        self.verticalLayout.addWidget(self.pushButton_particalsearch)

        self.MainWidget.addTab(self.Searchtab, "")
        self.Insertiontab = QWidget()
        self.Insertiontab.setObjectName(u"Insertiontab")
        self.stackedWidget_2 = QStackedWidget(self.Insertiontab)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 60, 511, 501))
        self.page_analysisnull = QWidget()
        self.page_analysisnull.setObjectName(u"page_analysisnull")
        self.stackedWidget_2.addWidget(self.page_analysisnull)
        self.page_authoranalysis = QWidget()
        self.page_authoranalysis.setObjectName(u"page_authoranalysis")
        self.layoutWidget_14 = QWidget(self.page_authoranalysis)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(110, 410, 261, 51))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yes_insert = QPushButton(self.layoutWidget_14)
        self.pushButton_yes_insert.setObjectName(u"pushButton_yes_insert")

        self.horizontalLayout_20.addWidget(self.pushButton_yes_insert)

        self.pushButton_back_insert = QPushButton(self.layoutWidget_14)
        self.pushButton_back_insert.setObjectName(u"pushButton_back_insert")

        self.horizontalLayout_20.addWidget(self.pushButton_back_insert)

        self.layoutWidget5 = QWidget(self.page_authoranalysis)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 50, 491, 311))
        self.verticalLayout_26 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_name = QLabel(self.layoutWidget5)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_15.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget5)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_15.addWidget(self.lineEdit_name)


        self.horizontalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_gjc = QLabel(self.layoutWidget5)
        self.label_gjc.setObjectName(u"label_gjc")

        self.verticalLayout_16.addWidget(self.label_gjc)

        self.lineEdit_gjc = QLineEdit(self.layoutWidget5)
        self.lineEdit_gjc.setObjectName(u"lineEdit_gjc")

        self.verticalLayout_16.addWidget(self.lineEdit_gjc)


        self.horizontalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_date = QLabel(self.layoutWidget5)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_17.addWidget(self.label_date)

        self.lineEdit_date = QLineEdit(self.layoutWidget5)
        self.lineEdit_date.setObjectName(u"lineEdit_date")

        self.verticalLayout_17.addWidget(self.lineEdit_date)


        self.horizontalLayout_17.addLayout(self.verticalLayout_17)


        self.verticalLayout_26.addLayout(self.horizontalLayout_17)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_author = QLabel(self.layoutWidget5)
        self.label_author.setObjectName(u"label_author")

        self.verticalLayout_18.addWidget(self.label_author)

        self.lineEdit_author = QLineEdit(self.layoutWidget5)
        self.lineEdit_author.setObjectName(u"lineEdit_author")

        self.verticalLayout_18.addWidget(self.lineEdit_author)


        self.verticalLayout_25.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_author_3 = QLabel(self.layoutWidget5)
        self.label_author_3.setObjectName(u"label_author_3")

        self.verticalLayout_19.addWidget(self.label_author_3)

        self.lineEdit_author_3 = QLineEdit(self.layoutWidget5)
        self.lineEdit_author_3.setObjectName(u"lineEdit_author_3")

        self.verticalLayout_19.addWidget(self.lineEdit_author_3)


        self.verticalLayout_25.addLayout(self.verticalLayout_19)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_tag = QLabel(self.layoutWidget5)
        self.label_tag.setObjectName(u"label_tag")

        self.verticalLayout_20.addWidget(self.label_tag)

        self.lineEdit_tag = QLineEdit(self.layoutWidget5)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")

        self.verticalLayout_20.addWidget(self.lineEdit_tag)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_src = QLabel(self.layoutWidget5)
        self.label_src.setObjectName(u"label_src")

        self.verticalLayout_21.addWidget(self.label_src)

        self.lineEdit_src = QLineEdit(self.layoutWidget5)
        self.lineEdit_src.setObjectName(u"lineEdit_src")

        self.verticalLayout_21.addWidget(self.lineEdit_src)


        self.horizontalLayout_19.addLayout(self.verticalLayout_21)


        self.verticalLayout_26.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_journalname = QLabel(self.layoutWidget5)
        self.label_journalname.setObjectName(u"label_journalname")

        self.verticalLayout_22.addWidget(self.label_journalname)

        self.lineEdit_journalname = QLineEdit(self.layoutWidget5)
        self.lineEdit_journalname.setObjectName(u"lineEdit_journalname")

        self.verticalLayout_22.addWidget(self.lineEdit_journalname)


        self.horizontalLayout_18.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labe_journalid = QLabel(self.layoutWidget5)
        self.labe_journalid.setObjectName(u"labe_journalid")

        self.verticalLayout_23.addWidget(self.labe_journalid)

        self.lineEdit_journalid = QLineEdit(self.layoutWidget5)
        self.lineEdit_journalid.setObjectName(u"lineEdit_journalid")

        self.verticalLayout_23.addWidget(self.lineEdit_journalid)


        self.horizontalLayout_18.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_journalpage = QLabel(self.layoutWidget5)
        self.label_journalpage.setObjectName(u"label_journalpage")

        self.verticalLayout_24.addWidget(self.label_journalpage)

        self.lineEdit_journalpage = QLineEdit(self.layoutWidget5)
        self.lineEdit_journalpage.setObjectName(u"lineEdit_journalpage")

        self.verticalLayout_24.addWidget(self.lineEdit_journalpage)


        self.horizontalLayout_18.addLayout(self.verticalLayout_24)


        self.verticalLayout_26.addLayout(self.horizontalLayout_18)

        self.stackedWidget_2.addWidget(self.page_authoranalysis)
        self.MainWidget.addTab(self.Insertiontab, "")

        self.retranslateUi(Form)

        self.MainWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_basicsearch.setCurrentIndex(-1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)

        '-------------------------------槽函数连接处-------------------------------'
        self.pushButton_exit.clicked.connect(Form.close)
        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)
        self.pushButton_signin.clicked.connect(self.on_pushButton_register_clicked)
        self.pushButton_adminspace.clicked.connect(self.on_pushButton_admin_clicked)
        self.pushButton_basicsearch.clicked.connect(self.on_basicsearch_clicked)
        self.pushButton_particalsearch.clicked.connect(self.on_pushButton_particalsearch_clicked)
        self.pushButton_yes_register.clicked.connect(self.on_pushButton_yes_register_clicked)
        self.pushButton_back_register.clicked.connect(self.on_pushButton_back_register_clicked)
        self.pushButton_bs1.clicked.connect(self.on_pushButton_bs1_clicked)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_main1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">\u79d1\u5b66\u6587\u732e\u7ba1\u7406\u7cfb\u7edf</span></p></body></html>", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label_name2.setText(QCoreApplication.translate("Form", u"\u90b5\u5f08", None))
        self.label_name3.setText(QCoreApplication.translate("Form", u"\u6f58\u6cfd\u8f69", None))
        self.label_name1.setText(QCoreApplication.translate("Form", u"\u674e\u704f\u7199", None))
        self.label_name1_2.setText(QCoreApplication.translate("Form", u"\u9648\u4fca\u5c79", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.label_account_login.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\uff1a", None))
        self.label_password_login.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a", None))
        self.lineEdit_password_login.setText("")
        self.pushButton_yes_login.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton_back_login.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_account_register.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\uff1a       ", None))
        self.label_password_register.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a       ", None))
        self.lineEdit_password_register.setText("")
        self.label_password_2_register.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.lineEdit_password_2_register.setText("")
        self.pushButton_yes_register.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.pushButton_back_register.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_account_admin.setText(QCoreApplication.translate("Form", u"\u9700\u8981\u4fee\u6539\u7684\u7528\u6237\uff1a", None))
        self.label_grade.setText(QCoreApplication.translate("Form", u"\u65b0\u7684\u6743\u9650\u7b49\u7ea7\uff1a   ", None))
        self.lineEdit_grade.setText("")
        self.pushButton_rewrite.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.pushButton_back_admin.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.pushButton_login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_signin.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.pushButton_adminspace.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u7a7a\u95f4", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Logintab), QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.comboBox_basicsearch.setItemText(0, QCoreApplication.translate("Form", u"\u4f5c\u8005", None))
        self.comboBox_basicsearch.setItemText(1, QCoreApplication.translate("Form", u"\u8bba\u6587", None))
        self.comboBox_basicsearch.setItemText(2, QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd", None))
        self.comboBox_basicsearch.setItemText(3, QCoreApplication.translate("Form", u"\u671f\u520a", None))
        self.comboBox_basicsearch.setItemText(4, QCoreApplication.translate("Form", u"\u6807\u7b7e", None))

        self.comboBox_basicsearch.setCurrentText("")
        self.lineEdit_basicsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5b8c\u6574\u67e5\u8be2\u5185\u5bb9", None))
        self.pushButton_bs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.radioButton_particalsearch.setText(QCoreApplication.translate("Form", u"\u7cbe\u786e\u641c\u7d22", None))
        self.lineEdit_particalsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5173\u952e\u5b57\u4fe1\u606f", None))
        self.pushButton_ps1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_basicsearch.setText(QCoreApplication.translate("Form", u"\u57fa\u672c\u641c\u7d22", None))
        self.pushButton_particalsearch.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5339\u914d\u641c\u7d22", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Searchtab), QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.pushButton_yes_insert.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.pushButton_back_insert.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u540d\u79f0\uff1a", None))
        self.label_gjc.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\uff1a", None))
        self.label_date.setText(QCoreApplication.translate("Form", u"\u53d1\u8868\u65e5\u671f\uff08yy-MM-dd\uff09\uff1a", None))
        self.label_author.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u7b2c\u4e00\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a", None))
        self.label_author_3.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u7b2c\u4e8c\u4f5c\u8005\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a", None))
        self.label_tag.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u6807\u7b7e\uff08\u6709\u591a\u4e2a\u8bf7\u4ee5\u82f1\u6587\u9017\u53f7\u9694\u5f00\uff09\uff1a", None))
        self.label_src.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u6765\u6e90\uff1a", None))
        self.label_journalname.setText(QCoreApplication.translate("Form", u"\u6587\u6863\u671f\u520a\u540d\u79f0\uff1a", None))
        self.labe_journalid.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u671f\u53f7\uff1a", None))
        self.label_journalpage.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u9875\u6570\uff1a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Insertiontab), QCoreApplication.translate("Form", u"\u63d2\u5165", None))
    # retranslateUi

    '--------------------------函数处--------------------------------'

    # 按钮一：打开第一个面板
    def on_pushButton_login_clicked(self):
            self.pushButton_login.setVisible(True)
            username=self.lineEdit_account_login.text()
            password=self.lineEdit_password_login.text()
            if username=="" or password=="":
                QMessageBox.warning(self.page_login, "Warning", "用户名或密码不能为空！")
                return

            (result,userid,permission)=login_query(cursor,username,password)
            if result:
                    QMessageBox.information(self.page_login, "Information", "登录成功！")
                    user_id=userid
                    user_lvl=permission
            else:
                    QMessageBox.warning(self.page_login, "Warning", "用户名或密码错误！")

            self.stackedWidget_3.setCurrentIndex(1)

    def on_pushButton_register_clicked(self):
            self.pushButton_login.setVisible(False)#禁用登录按钮
            self.stackedWidget_3.setCurrentIndex(2)


    def on_pushButton_yes_register_clicked(self):
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
                    QMessageBox.information(self.page_register, "Information", "注册成功！")
                    user_id = userid
                    user_lvl = 1
                    self.stackedWidget_3.setCurrentIndex(1)
                    self.pushButton_login.setVisible(True)
            else:
                    QMessageBox.warning(self.page_register, "Warning", "用户名已存在！")
                    return
    def on_pushButton_back_register_clicked(self):
            self.stackedWidget_3.setCurrentIndex(1)
            self.pushButton_login.setVisible(True)

    def on_pushButton_admin_clicked(self):
            if user_lvl < ADMIN_LEVEL:
                    QMessageBox.warning(self.page_login, "Warning", "非管理员禁止访问！")
                    return
            self.stackedWidget_3.setCurrentIndex(3)

    def on_basicsearch_clicked(self):
            self.stackedWidget.setCurrentIndex(1)

    def on_pushButton_bs1_clicked(self):
        content=self.lineEdit_basicsearch.text()
        choice=self.comboBox_basicsearch.currentIndex()
        print(choice)
        result = []
        if choice ==-1 or choice == 1:
                result=query_with_title(cursor,content)
        elif choice ==0:
                result=query_with_authorname(cursor,content)
        elif choice ==2: #还没写关键词检索
                result="暂未开通"
        elif choice ==3:
                result=query_with_journalname(cursor,content)
        elif choice ==4:
                result=query_with_tag(cursor,content)
        print(result)
        # 把结果显示到页面上


    def on_pushButton_particalsearch_clicked(self):
            self.stackedWidget.setCurrentIndex(2)


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

