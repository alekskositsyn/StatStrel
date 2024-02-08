# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addOfficerDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(300, 446)
        dialog.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.dateEdit = QDateEdit(dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 12, 0, 1, 1)

        self.btnAdd = QPushButton(dialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 13, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(121, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 13, 1, 1, 1)

        self.btnCancel = QPushButton(dialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.gridLayout.addWidget(self.btnCancel, 13, 2, 1, 1)

        self.txtFirstName = QLineEdit(dialog)
        self.txtFirstName.setObjectName(u"txtFirstName")

        self.gridLayout.addWidget(self.txtFirstName, 1, 0, 1, 3)

        self.txtLastName = QLineEdit(dialog)
        self.txtLastName.setObjectName(u"txtLastName")

        self.gridLayout.addWidget(self.txtLastName, 3, 0, 1, 3)

        self.txtMiddleName = QLineEdit(dialog)
        self.txtMiddleName.setObjectName(u"txtMiddleName")

        self.gridLayout.addWidget(self.txtMiddleName, 5, 0, 1, 3)

        self.txtIdentityNum = QLineEdit(dialog)
        self.txtIdentityNum.setObjectName(u"txtIdentityNum")

        self.gridLayout.addWidget(self.txtIdentityNum, 7, 0, 1, 3)

        self.RBIsOperator = QRadioButton(dialog)
        self.RBIsOperator.setObjectName(u"RBIsOperator")

        self.gridLayout.addWidget(self.RBIsOperator, 12, 2, 1, 1)

        self.cmbDivisions = QComboBox(dialog)
        self.cmbDivisions.setObjectName(u"cmbDivisions")

        self.gridLayout.addWidget(self.cmbDivisions, 10, 0, 1, 3)

        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_5 = QLabel(dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 3)

        self.label_6 = QLabel(dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 3)

        self.label_7 = QLabel(dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 3)

        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 3)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.btnAdd.setText(QCoreApplication.translate("dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.RBIsOperator.setText(QCoreApplication.translate("dialog", u"\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440*", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f *", None))
        self.label_5.setText(QCoreApplication.translate("dialog", u"\u0418\u043c\u044f *", None))
        self.label_6.setText(QCoreApplication.translate("dialog", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("dialog", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

