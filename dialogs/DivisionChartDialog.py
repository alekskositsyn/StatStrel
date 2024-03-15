# coding: utf-8
from PySide6 import QtCharts
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow

from common.calc_mid_divisions import calc_mid_divisions
from common.get_division_degree import get_division_degree
from data.create_session import create_session_to_mysql
from user_interface.devision_chart_ui import Ui_DivChartDialog


class DivisionChart(QDialog):
    def __init__(self, divisions, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DivChartDialog()
        self.ui.setupUi(self)
        self.divisions = divisions
        self.config = config
        self.draw_divisions_bar_chart()

    def draw_divisions_bar_chart(self):
        chart = QtCharts.QChart()
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)

        series = QtCharts.QBarSeries()
        series.setName("Результаты подразделений")
        series.setLabelsVisible()
        series.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideEnd)

        bar_set = QtCharts.QBarSet('Подразделения')
        bar_set.setColor("#3e3e3e")
        # bar_set.setLabelColor('#3e3e3e')

        divisions_names = []
        result = []

        for division in self.divisions.values():
            divisions_names.append(division.name)
            with create_session_to_mysql(self.config) as s:
                # получаем список сотрудников с их уровнем подготовки
                degree = get_division_degree(s, division.id)
                result.append(degree)
        #     with create_session() as s:
        #         rows = fetch_task_4(s, division.id)
        #         result = calc_mid_divisions(rows)
        bar_set.append(result)
        #     # Цвет результата на столбце
        #     # bar_set.setLabelColor('#3e3e3e')
        #     # Цвет столбца
        #     # bar_set.setColor("#3e3e3e")
        #     # Позиция результата на столбце
        series.append(bar_set)

        chart.addSeries(series)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(divisions_names)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Проценты")
        axis_y.setMax(100)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Set the chart view's chart
        # chart_view.setChart(chart)

        # chart.createDefaultAxes()
        # Создаем названия столбцам
        # axis = QtCharts.QBarCategoryAxis()
        # axis.append(['Подразделения'])
        # chart.setAxisX(axis)
        # series.attachAxis(axis)

        self.ui.chartView.setChart(chart)
