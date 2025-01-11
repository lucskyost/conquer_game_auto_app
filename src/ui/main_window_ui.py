# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 769)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1157, 793))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1117, 800))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1140, 750))
        self.widget.setMinimumSize(QSize(1140, 750))
        self.widget.setMaximumSize(QSize(1140, 750))
        self.widget.setStyleSheet(u"background-color:#338eff;\n"
"\n"
"")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QRect(24, 21, 971, 701))
        self.graphicsView.setStyleSheet(u"QFrame {\n"
"    background-color: #2d3349;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.graphicsView_2 = QGraphicsView(self.widget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(25, 21, 181, 701))
        self.graphicsView_2.setStyleSheet(u"\n"
"QFrame {\n"
"    background-color: #181d36; /* M\u00e0u n\u1ec1n */\n"
"    color: #282a36; /* M\u00e0u v\u0103n b\u1ea3n */\n"
"    border-top-left-radius: 25px; /* \u0110\u1eb7t b\u00e1n k\u00ednh bo tr\u00f2n cho g\u00f3c tr\u00ean c\u00f9ng b\u00ean tr\u00e1i */\n"
"    border-bottom-left-radius: 25px; /* \u0110\u1eb7t b\u00e1n k\u00ednh bo tr\u00f2n cho g\u00f3c d\u01b0\u1edbi c\u00f9ng b\u00ean tr\u00e1i */\n"
"}\n"
"")
        self.avatar_label = QLabel(self.widget)
        self.avatar_label.setObjectName(u"avatar_label")
        self.avatar_label.setGeometry(QRect(65, 50, 101, 101))
        self.avatar_label.setStyleSheet(u"background-color: #181d36;\n"
"image: url(:/images/images/default_avatar.png);")
        self.avatar_label.setPixmap(QPixmap(u":/images/images/default_avatar.png"))
        self.avatar_label.setScaledContents(True)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(45, 170, 141, 191))
        self.frame.setStyleSheet(u"background-color: #181d36; \n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"color: #dadbdf;\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/genera_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: #dadbdf;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/contact_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.updateButton = QPushButton(self.frame)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setStyleSheet(u"color: #dadbdf;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/adress_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon2)

        self.verticalLayout.addWidget(self.updateButton)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: #dadbdf;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(206, 0, 811, 726))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(28, 87, 731, 611))
        self.frame_3.setStyleSheet(u"background-color: #181d36;\n"
"border-radius: 25px;\n"
"color: #dadbdf;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(19, 20, 743, 591))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 711, 71))
        self.frame_5.setStyleSheet(u"\n"
"border-radius: 0;\n"
"/*border-bottom: 1px solid #338eff;*/\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.sortButton = QPushButton(self.frame_5)
        self.sortButton.setObjectName(u"sortButton")
        self.sortButton.setGeometry(QRect(620, 10, 75, 24))
        self.sortButton.setStyleSheet(u" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/sort_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sortButton.setIcon(icon4)
        self.reloadButton = QPushButton(self.frame_5)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setGeometry(QRect(530, 10, 75, 24))
        self.reloadButton.setStyleSheet(u" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/reload_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadButton.setIcon(icon5)
        self.sellectAllCheckBox = QCheckBox(self.frame_5)
        self.sellectAllCheckBox.setObjectName(u"sellectAllCheckBox")
        self.sellectAllCheckBox.setGeometry(QRect(26, 55, 76, 20))
        self.importButton = QPushButton(self.frame_5)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(440, 10, 75, 24))
        self.importButton.setStyleSheet(u" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/import_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importButton.setIcon(icon6)
        self.importFileLabel = QLabel(self.frame_5)
        self.importFileLabel.setObjectName(u"importFileLabel")
        self.importFileLabel.setGeometry(QRect(0, 10, 101, 24))
        self.importFileLabel.setStyleSheet(u"\n"
"\n"
"border-bottom: 1px solid #338eff;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"\n"
"\n"
"")
        self.importFileLabel.setWordWrap(False)
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-5, 80, 701, 251))
        self.tableWidget.setMaximumSize(QSize(751, 251))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"               background-color: #181d36; /* M\u00e0u n\u1ec1n c\u1ee7a header */\n"
"			   /*color:#dadbdf;*/\n"
"			   color: #dadbdf;\n"
"            };\n"
"border-radius: 0;\n"
"border-top: 1px solid #338eff;\n"
"border-bottom: 1px solid #338eff;\n"
"\n"
"\n"
"")
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(93)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 349, 711, 241))
        self.frame_6.setStyleSheet(u"color: #fff")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(17, 30, 451, 35))
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(6500, 16777215))
        self.frame_7.setStyleSheet(u"\n"
"background-color: rgb(24, 29, 54);\n"
"border-radius:0;\n"
"QFrame{\n"
"     border-bottom: 1px solid #000000;\n"
"	 border-top: 0px;\n"
"	 border-right: 0px;\n"
"	 border-left: 0px;}\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.runAutoFileCheckBox1 = QCheckBox(self.frame_7)
        self.runAutoFileCheckBox1.setObjectName(u"runAutoFileCheckBox1")
        self.runAutoFileCheckBox1.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.runAutoFileCheckBox1)

        self.autoFileLabel1 = QLabel(self.frame_7)
        self.autoFileLabel1.setObjectName(u"autoFileLabel1")
        self.autoFileLabel1.setStyleSheet(u"border-bottom: 1px solid #338eff;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"")

        self.horizontalLayout.addWidget(self.autoFileLabel1)

        self.chosseFileButton1 = QPushButton(self.frame_7)
        self.chosseFileButton1.setObjectName(u"chosseFileButton1")
        self.chosseFileButton1.setStyleSheet(u"\n"
"\n"
" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border-bottom: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/folder_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chosseFileButton1.setIcon(icon7)

        self.horizontalLayout.addWidget(self.chosseFileButton1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(5, 162, 743, 71))
        self.frame_8.setMinimumSize(QSize(641, 0))
        self.frame_8.setMaximumSize(QSize(6500, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-radius:0;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.runButton = QPushButton(self.frame_8)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(620, 30, 75, 24))
        self.runButton.setStyleSheet(u" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/rocket_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runButton.setIcon(icon8)
        self.closeAllButon = QPushButton(self.frame_8)
        self.closeAllButon.setObjectName(u"closeAllButon")
        self.closeAllButon.setGeometry(QRect(530, 30, 75, 24))
        self.closeAllButon.setStyleSheet(u" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAllButon.setIcon(icon9)
        self.loginCheckBox = QCheckBox(self.frame_6)
        self.loginCheckBox.setObjectName(u"loginCheckBox")
        self.loginCheckBox.setGeometry(QRect(26, 0, 76, 20))
        self.buyItemCheckBox = QCheckBox(self.frame_6)
        self.buyItemCheckBox.setObjectName(u"buyItemCheckBox")
        self.buyItemCheckBox.setGeometry(QRect(26, 71, 76, 20))
        self.waitingSpinnerLabel = QLabel(self.frame_6)
        self.waitingSpinnerLabel.setObjectName(u"waitingSpinnerLabel")
        self.waitingSpinnerLabel.setGeometry(QRect(641, 140, 41, 41))
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(17, 100, 451, 35))
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(6500, 16777215))
        self.frame_9.setStyleSheet(u"\n"
"background-color: rgb(24, 29, 54);\n"
"border-radius:0;\n"
"QFrame{\n"
"     border-bottom: 1px solid #000000;\n"
"	 border-top: 0px;\n"
"	 border-right: 0px;\n"
"	 border-left: 0px;}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.runAutoFileCheckBox2 = QCheckBox(self.frame_9)
        self.runAutoFileCheckBox2.setObjectName(u"runAutoFileCheckBox2")
        self.runAutoFileCheckBox2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.runAutoFileCheckBox2)

        self.autoFileLabel2 = QLabel(self.frame_9)
        self.autoFileLabel2.setObjectName(u"autoFileLabel2")
        self.autoFileLabel2.setStyleSheet(u"border-bottom: 1px solid #338eff;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.autoFileLabel2)

        self.chosseFileButton2 = QPushButton(self.frame_9)
        self.chosseFileButton2.setObjectName(u"chosseFileButton2")
        self.chosseFileButton2.setStyleSheet(u"\n"
"\n"
" QPushButton {\n"
"border-radius: 10px; /* \u0110i\u1ec1u ch\u1ec9nh gi\u00e1 tr\u1ecb s\u1ed1 px t\u00f9y theo m\u1ee9c \u0111\u1ed9 bo tr\u00f2n mong mu\u1ed1n */\n"
"\n"
"border-bottom: 1px solid #338eff;\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            }\n"
"\n"
" /* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n */\n"
"            QPushButton:pressed {\n"
"                background-color: #338eff; /* M\u00e0u n\u1ec1n khi nh\u1ea5n */\n"
"				   \n"
"            }\n"
"\n"
"\n"
"\n"
"")
        self.chosseFileButton2.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.chosseFileButton2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 1022, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        self.centralwidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.avatar_label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GENERAL", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CONTACT", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SETTING", None))
        self.sortButton.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.reloadButton.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.sellectAllCheckBox.setText(QCoreApplication.translate("MainWindow", u"Sellect all", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.importFileLabel.setText(QCoreApplication.translate("MainWindow", u"Import File: None", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"USER", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"GROUP", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SERVER", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"LEVEL", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"GOLD", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.runAutoFileCheckBox1.setText(QCoreApplication.translate("MainWindow", u"Run auto file 1", None))
        self.autoFileLabel1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.chosseFileButton1.setText(QCoreApplication.translate("MainWindow", u"Chosse File", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.closeAllButon.setText(QCoreApplication.translate("MainWindow", u"Close All", None))
        self.loginCheckBox.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.buyItemCheckBox.setText(QCoreApplication.translate("MainWindow", u"Buy item", None))
        self.waitingSpinnerLabel.setText("")
        self.runAutoFileCheckBox2.setText(QCoreApplication.translate("MainWindow", u"Run auto file 2", None))
        self.autoFileLabel2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.chosseFileButton2.setText(QCoreApplication.translate("MainWindow", u"Chosse File", None))
    # retranslateUi

