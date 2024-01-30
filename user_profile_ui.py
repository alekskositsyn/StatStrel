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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(961, 361)
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_widget = QWidget(Dialog)
        self.left_widget.setObjectName(u"left_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.left_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableView = QTableView(self.left_widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(210, 320))

        self.horizontalLayout_2.addWidget(self.tableView)


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
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblName_5 = QLabel(self.frame_2)
        self.lblName_5.setObjectName(u"lblName_5")
        font = QFont()
        font.setStrikeOut(False)
        self.lblName_5.setFont(font)
        self.lblName_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName_5)

        self.userChartView = QChartView(self.frame_2)
        self.userChartView.setObjectName(u"userChartView")

        self.verticalLayout.addWidget(self.userChartView)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(551, 88))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblName = QLabel(self.frame_3)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setFont(font)
        self.lblName.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblName, 0, 0, 1, 1)

        self.txtName = QLineEdit(self.frame_3)
        self.txtName.setObjectName(u"txtName")

        self.gridLayout_2.addWidget(self.txtName, 0, 1, 1, 1)

        self.lblName_2 = QLabel(self.frame_3)
        self.lblName_2.setObjectName(u"lblName_2")
        self.lblName_2.setFont(font)
        self.lblName_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblName_2, 1, 0, 1, 1)

        self.txtDivision = QLineEdit(self.frame_3)
        self.txtDivision.setObjectName(u"txtDivision")

        self.gridLayout_2.addWidget(self.txtDivision, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblName_3 = QLabel(self.frame_4)
        self.lblName_3.setObjectName(u"lblName_3")
        self.lblName_3.setFont(font)
        self.lblName_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblName_3, 0, 0, 1, 1)

        self.lblName_4 = QLabel(self.frame_4)
        self.lblName_4.setObjectName(u"lblName_4")
        self.lblName_4.setFont(font)
        self.lblName_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblName_4, 1, 0, 1, 2)

        self.txtDegree = QLineEdit(self.frame_4)
        self.txtDegree.setObjectName(u"txtDegree")

        self.gridLayout_3.addWidget(self.txtDegree, 1, 2, 1, 1)

        self.txtBDate = QLineEdit(self.frame_4)
        self.txtBDate.setObjectName(u"txtBDate")

        self.gridLayout_3.addWidget(self.txtBDate, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblName_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblName.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblName_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.lblName_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.lblName_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0435\u043b\u043a\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
    # retranslateUi

