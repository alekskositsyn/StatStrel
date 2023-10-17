# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(596, 656)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout.addWidget(self.btn_add, 5, 1, 1, 1)

        self.cmb_division = QComboBox(self.frame)
        self.cmb_division.setObjectName(u"cmb_division")

        self.gridLayout.addWidget(self.cmb_division, 2, 1, 1, 1)

        self.tblItems = QTableView(self.frame)
        self.tblItems.setObjectName(u"tblItems")

        self.gridLayout.addWidget(self.tblItems, 4, 1, 1, 4)

        self.cmb_degree = QComboBox(self.frame)
        self.cmb_degree.setObjectName(u"cmb_degree")

        self.gridLayout.addWidget(self.cmb_degree, 2, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.btn_update = QPushButton(self.frame)
        self.btn_update.setObjectName(u"btn_update")

        self.gridLayout.addWidget(self.btn_update, 5, 2, 1, 1)

        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 5, 3, 1, 1)

        self.cmbTasks = QComboBox(self.frame)
        self.cmbTasks.setObjectName(u"cmbTasks")

        self.gridLayout.addWidget(self.cmbTasks, 2, 3, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 596, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

