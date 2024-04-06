# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parsing_file_path.ui'
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
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ParsingFilePath(object):
    def setupUi(self, ParsingFilePath):
        if not ParsingFilePath.objectName():
            ParsingFilePath.setObjectName(u"ParsingFilePath")
        ParsingFilePath.resize(550, 183)
        ParsingFilePath.setMinimumSize(QSize(350, 183))
        ParsingFilePath.setMaximumSize(QSize(550, 183))
        self.verticalLayout = QVBoxLayout(ParsingFilePath)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ParsingFilePath)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.file_path_field = QLineEdit(self.frame)
        self.file_path_field.setObjectName(u"file_path_field")

        self.horizontalLayout_2.addWidget(self.file_path_field)


        self.verticalLayout.addWidget(self.frame)

        self.btn_path = QPushButton(ParsingFilePath)
        self.btn_path.setObjectName(u"btn_path")

        self.verticalLayout.addWidget(self.btn_path)

        self.frame_2 = QFrame(ParsingFilePath)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_check_file = QPushButton(self.frame_2)
        self.btn_check_file.setObjectName(u"btn_check_file")

        self.horizontalLayout.addWidget(self.btn_check_file)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(ParsingFilePath)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.btn_save = QPushButton(self.frame_3)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.btn_cancle = QPushButton(self.frame_3)
        self.btn_cancle.setObjectName(u"btn_cancle")

        self.horizontalLayout_3.addWidget(self.btn_cancle)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(ParsingFilePath)

        QMetaObject.connectSlotsByName(ParsingFilePath)
    # setupUi

    def retranslateUi(self, ParsingFilePath):
        ParsingFilePath.setWindowTitle(QCoreApplication.translate("ParsingFilePath", u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430", None))
        self.label.setText(QCoreApplication.translate("ParsingFilePath", u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430:", None))
        self.btn_path.setText(QCoreApplication.translate("ParsingFilePath", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.btn_check_file.setText(QCoreApplication.translate("ParsingFilePath", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.btn_save.setText(QCoreApplication.translate("ParsingFilePath", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancle.setText(QCoreApplication.translate("ParsingFilePath", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

