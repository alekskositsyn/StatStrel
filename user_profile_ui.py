# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_profile_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(816, 478)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblName = QLabel(self.frame)
        self.lblName.setObjectName(u"lblName")
        font = QFont()
        font.setStrikeOut(False)
        self.lblName.setFont(font)
        self.lblName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName)

        self.txtName = QLineEdit(self.frame)
        self.txtName.setObjectName(u"txtName")

        self.verticalLayout.addWidget(self.txtName)

        self.lblName_2 = QLabel(self.frame)
        self.lblName_2.setObjectName(u"lblName_2")
        self.lblName_2.setFont(font)
        self.lblName_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName_2)

        self.txtDivision = QLineEdit(self.frame)
        self.txtDivision.setObjectName(u"txtDivision")

        self.verticalLayout.addWidget(self.txtDivision)

        self.lblName_3 = QLabel(self.frame)
        self.lblName_3.setObjectName(u"lblName_3")
        self.lblName_3.setFont(font)
        self.lblName_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName_3)

        self.txtBDate = QLineEdit(self.frame)
        self.txtBDate.setObjectName(u"txtBDate")

        self.verticalLayout.addWidget(self.txtBDate)

        self.lblName_4 = QLabel(self.frame)
        self.lblName_4.setObjectName(u"lblName_4")
        self.lblName_4.setFont(font)
        self.lblName_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName_4)

        self.txtDegree = QLineEdit(self.frame)
        self.txtDegree.setObjectName(u"txtDegree")

        self.verticalLayout.addWidget(self.txtDegree)

        self.lblName_6 = QLabel(self.frame)
        self.lblName_6.setObjectName(u"lblName_6")
        self.lblName_6.setFont(font)
        self.lblName_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblName_6)

        self.cmbTasks = QComboBox(self.frame)
        self.cmbTasks.setObjectName(u"cmbTasks")

        self.verticalLayout.addWidget(self.cmbTasks)

        self.splitter.addWidget(self.frame)
        self.line = QFrame(self.splitter)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.splitter.addWidget(self.line)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblName_5 = QLabel(self.frame_2)
        self.lblName_5.setObjectName(u"lblName_5")
        self.lblName_5.setFont(font)
        self.lblName_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblName_5, 0, 0, 1, 1)

        self.userChartView = QChartView(self.frame_2)
        self.userChartView.setObjectName(u"userChartView")

        self.gridLayout.addWidget(self.userChartView, 1, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblName.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.lblName_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.lblName_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.lblName_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0435\u043b\u043a\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.lblName_6.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f", None))
        self.lblName_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
    # retranslateUi

