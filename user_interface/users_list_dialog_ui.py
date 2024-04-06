# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usersListDialog.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_UsersListDialog(object):
    def setupUi(self, UsersListDialog):
        if not UsersListDialog.objectName():
            UsersListDialog.setObjectName(u"UsersListDialog")
        UsersListDialog.resize(489, 681)
        self.verticalLayout = QVBoxLayout(UsersListDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usersListWidget = QListWidget(UsersListDialog)
        self.usersListWidget.setObjectName(u"usersListWidget")

        self.verticalLayout.addWidget(self.usersListWidget)

        self.frame = QFrame(UsersListDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSave = QPushButton(self.frame)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(UsersListDialog)

        QMetaObject.connectSlotsByName(UsersListDialog)
    # setupUi

    def retranslateUi(self, UsersListDialog):
        UsersListDialog.setWindowTitle(QCoreApplication.translate("UsersListDialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btnSave.setText(QCoreApplication.translate("UsersListDialog", u"\u0412\u0441\u0451 \u041e\u043a", None))
        self.btnCancel.setText(QCoreApplication.translate("UsersListDialog", u"\u0427\u0451\u0442 \u043d\u0435 \u0442\u043e....", None))
    # retranslateUi

