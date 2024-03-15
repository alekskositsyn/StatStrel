# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(220, 360)
        SettingsDialog.setMinimumSize(QSize(220, 360))
        SettingsDialog.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SettingsDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.txtPort = QLineEdit(SettingsDialog)
        self.txtPort.setObjectName(u"txtPort")

        self.verticalLayout.addWidget(self.txtPort)

        self.label_address = QLabel(SettingsDialog)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setFont(font)
        self.label_address.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_address)

        self.txtAddress = QLineEdit(SettingsDialog)
        self.txtAddress.setObjectName(u"txtAddress")

        self.verticalLayout.addWidget(self.txtAddress)

        self.label_username = QLabel(SettingsDialog)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setFont(font)
        self.label_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_username)

        self.txtUsername = QLineEdit(SettingsDialog)
        self.txtUsername.setObjectName(u"txtUsername")

        self.verticalLayout.addWidget(self.txtUsername)

        self.label_name = QLabel(SettingsDialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)
        self.label_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_name)

        self.txtNameDB = QLineEdit(SettingsDialog)
        self.txtNameDB.setObjectName(u"txtNameDB")

        self.verticalLayout.addWidget(self.txtNameDB)

        self.label_pass = QLabel(SettingsDialog)
        self.label_pass.setObjectName(u"label_pass")
        self.label_pass.setFont(font)
        self.label_pass.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_pass)

        self.txtPass = QLineEdit(SettingsDialog)
        self.txtPass.setObjectName(u"txtPass")

        self.verticalLayout.addWidget(self.txtPass)

        self.frame = QFrame(SettingsDialog)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setBold(True)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnTestConn = QPushButton(self.frame)
        self.btnTestConn.setObjectName(u"btnTestConn")

        self.horizontalLayout.addWidget(self.btnTestConn)

        self.radioBtnOk = QRadioButton(self.frame)
        self.radioBtnOk.setObjectName(u"radioBtnOk")
        self.radioBtnOk.setCheckable(False)

        self.horizontalLayout.addWidget(self.radioBtnOk)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(SettingsDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.btnSave = QPushButton(self.frame_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnSave)

        self.btnCancel = QPushButton(self.frame_2)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(SettingsDialog)

        self.btnSave.setDefault(False)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"\u041f\u043e\u0440\u0442", None))
        self.txtPort.setText(QCoreApplication.translate("SettingsDialog", u"3123", None))
        self.label_address.setText(QCoreApplication.translate("SettingsDialog", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.txtAddress.setText(QCoreApplication.translate("SettingsDialog", u"localhost", None))
        self.label_username.setText(QCoreApplication.translate("SettingsDialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.txtUsername.setText(QCoreApplication.translate("SettingsDialog", u"name", None))
        self.label_name.setText(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.txtNameDB.setText(QCoreApplication.translate("SettingsDialog", u"dbname", None))
        self.label_pass.setText(QCoreApplication.translate("SettingsDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.txtPass.setText(QCoreApplication.translate("SettingsDialog", u"password", None))
        self.btnTestConn.setText(QCoreApplication.translate("SettingsDialog", u"\u0422\u0435\u0441\u0442\u043e\u0432\u043e\u0435 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.radioBtnOk.setText(QCoreApplication.translate("SettingsDialog", u"\u041e\u043a", None))
        self.btnSave.setText(QCoreApplication.translate("SettingsDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("SettingsDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

