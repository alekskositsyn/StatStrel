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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QTableView, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(861, 505)
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_widget = QWidget(Dialog)
        self.left_widget.setObjectName(u"left_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.left_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.table_user_profile = QTableView(self.left_widget)
        self.table_user_profile.setObjectName(u"table_user_profile")
        self.table_user_profile.setMinimumSize(QSize(220, 320))
        self.table_user_profile.setMaximumSize(QSize(220, 16777215))
        self.table_user_profile.horizontalHeader().setCascadingSectionResizes(False)
        self.table_user_profile.horizontalHeader().setDefaultSectionSize(48)
        self.table_user_profile.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.table_user_profile)


        self.horizontalLayout_3.addWidget(self.left_widget)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 250))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblName_5 = QLabel(self.frame_2)
        self.lblName_5.setObjectName(u"lblName_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblName_5.setFont(font)
        self.lblName_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblName_5, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(138, -1, -1, -1)
        self.lblBDate = QLabel(self.frame_6)
        self.lblBDate.setObjectName(u"lblBDate")
        self.lblBDate.setMaximumSize(QSize(91, 16777215))
        self.lblBDate.setFont(font)
        self.lblBDate.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblBDate, 0, 0, 1, 1)

        self.lblName_6 = QLabel(self.frame_6)
        self.lblName_6.setObjectName(u"lblName_6")
        self.lblName_6.setMinimumSize(QSize(0, 0))
        self.lblName_6.setMaximumSize(QSize(31, 16777215))
        self.lblName_6.setFont(font)
        self.lblName_6.setScaledContents(False)
        self.lblName_6.setAlignment(Qt.AlignCenter)
        self.lblName_6.setMargin(-1)

        self.gridLayout_3.addWidget(self.lblName_6, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 0, 0, 1, 1)

        self.txtDivision = QLabel(self.frame_5)
        self.txtDivision.setObjectName(u"txtDivision")
        self.txtDivision.setFont(font)
        self.txtDivision.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtDivision.setMargin(0)

        self.gridLayout_2.addWidget(self.txtDivision, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)

        self.userChartView = QChartView(self.frame_2)
        self.userChartView.setObjectName(u"userChartView")
        self.userChartView.setMinimumSize(QSize(580, 220))

        self.gridLayout.addWidget(self.userChartView, 1, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblName_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblBDate.setText(QCoreApplication.translate("Dialog", u"08.00.2134", None))
        self.lblName_6.setText(QCoreApplication.translate("Dialog", u"\u0433.\u0440.", None))
        self.txtDivision.setText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u0442\u0430\u043b\u044c\u043e\u043d", None))
    # retranslateUi

