# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_profile_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(781, 468)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_11 = QFrame(Dialog)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(240, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.frame_11)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblLastName = QLabel(self.frame)
        self.lblLastName.setObjectName(u"lblLastName")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblLastName.setFont(font)
        self.lblLastName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblLastName)

        self.lblFirstName = QLabel(self.frame)
        self.lblFirstName.setObjectName(u"lblFirstName")
        self.lblFirstName.setFont(font)
        self.lblFirstName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblFirstName)

        self.lblMiddleName = QLabel(self.frame)
        self.lblMiddleName.setObjectName(u"lblMiddleName")
        self.lblMiddleName.setFont(font)
        self.lblMiddleName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblMiddleName)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_11)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblBDate = QLabel(self.frame_6)
        self.lblBDate.setObjectName(u"lblBDate")
        self.lblBDate.setMaximumSize(QSize(300, 16777215))
        self.lblBDate.setFont(font)
        self.lblBDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblBDate)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.txtDivision = QLabel(self.frame_5)
        self.txtDivision.setObjectName(u"txtDivision")
        self.txtDivision.setMaximumSize(QSize(300, 16777215))
        self.txtDivision.setFont(font)
        self.txtDivision.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.txtDivision)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 2, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 1, 2, 1)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 250))
        self.frame_2.setMaximumSize(QSize(16777215, 250))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.userChartView = QChartView(self.frame_2)
        self.userChartView.setObjectName(u"userChartView")
        self.userChartView.setMinimumSize(QSize(500, 220))

        self.gridLayout_2.addWidget(self.userChartView, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 2, 1, 3)

        self.bottom_widget = QWidget(Dialog)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.gridLayout = QGridLayout(self.bottom_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.table_user_profile = QTableView(self.bottom_widget)
        self.table_user_profile.setObjectName(u"table_user_profile")
        self.table_user_profile.setMinimumSize(QSize(20, 20))
        self.table_user_profile.setMaximumSize(QSize(16777215, 16777215))
        self.table_user_profile.horizontalHeader().setCascadingSectionResizes(False)
        self.table_user_profile.horizontalHeader().setDefaultSectionSize(48)
        self.table_user_profile.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table_user_profile, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.bottom_widget, 1, 3, 1, 1)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(220, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.txtPoints = QLineEdit(self.frame_4)
        self.txtPoints.setObjectName(u"txtPoints")
        self.txtPoints.setAlignment(Qt.AlignCenter)
        self.txtPoints.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.txtPoints)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.txtCount = QLineEdit(self.frame_7)
        self.txtCount.setObjectName(u"txtCount")
        self.txtCount.setAlignment(Qt.AlignCenter)
        self.txtCount.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.txtCount)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.txtTime = QLineEdit(self.frame_8)
        self.txtTime.setObjectName(u"txtTime")
        self.txtTime.setAlignment(Qt.AlignCenter)
        self.txtTime.setReadOnly(False)

        self.verticalLayout_5.addWidget(self.txtTime)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.frame_9)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEdit)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.btnInsertData = QPushButton(self.frame_3)
        self.btnInsertData.setObjectName(u"btnInsertData")

        self.verticalLayout_6.addWidget(self.btnInsertData)


        self.gridLayout_3.addWidget(self.frame_3, 1, 4, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblLastName.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lblFirstName.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.lblMiddleName.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.lblBDate.setText(QCoreApplication.translate("Dialog", u"08.01.2004", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.txtDivision.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b-\u0432\u043e\n"
"\u043f\u043e\u043f\u0430\u0434\u0430\u043d\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b-\u0432\u043e\n"
"\u0432\u044b\u0441\u0442\u0440\u0435\u043b\u043e\u0432", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f\n"
"\u0441\u0435\u043a.", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.btnInsertData.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

