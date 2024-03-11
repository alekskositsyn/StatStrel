# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'div_chart_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QWidget)

class Ui_DivChartDialog(object):
    def setupUi(self, DivChartDialog):
        if not DivChartDialog.objectName():
            DivChartDialog.setObjectName(u"DivChartDialog")
        DivChartDialog.resize(400, 300)
        self.gridLayout = QGridLayout(DivChartDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chartView = QChartView(DivChartDialog)
        self.chartView.setObjectName(u"chartView")

        self.gridLayout.addWidget(self.chartView, 0, 0, 1, 1)


        self.retranslateUi(DivChartDialog)

        QMetaObject.connectSlotsByName(DivChartDialog)
    # setupUi

    def retranslateUi(self, DivChartDialog):
        DivChartDialog.setWindowTitle(QCoreApplication.translate("DivChartDialog", u"Dialog", None))
    # retranslateUi

