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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(316, 314)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtName = QLineEdit(Dialog)
        self.txtName.setObjectName(u"txtName")

        self.gridLayout.addWidget(self.txtName, 1, 0, 1, 3)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.cmbDivisions = QComboBox(Dialog)
        self.cmbDivisions.setObjectName(u"cmbDivisions")

        self.gridLayout.addWidget(self.cmbDivisions, 3, 0, 1, 3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 2)

        self.cmbDegree = QComboBox(Dialog)
        self.cmbDegree.setObjectName(u"cmbDegree")

        self.gridLayout.addWidget(self.cmbDegree, 7, 0, 1, 3)

        self.btnAdd = QPushButton(Dialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 8, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(121, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 1, 1, 1)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.gridLayout.addWidget(self.btnCancel, 8, 2, 1, 1)

        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 5, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0424.\u0418.\u041e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0435\u043b\u043a\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

