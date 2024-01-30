from PySide6 import QtCharts, QtWidgets
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore

from data.create_session import create_session
from data.fetch_task_results_by_user_id import fetch_task_results_by_user_id
from table_models.user_profile_table_model import UserProfileTableModel
from user_profile_ui import Ui_Dialog


class UserProfileDialog(QDialog):
    def __init__(self, degree, divisions, init_data, tasks, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = UserProfileTableModel()
        self.ui.table_user_profile.setModel(self.model)
        self.ui.table_user_profile.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)



        self.officer_id = init_data.id
        officer_name = init_data.user
        officers_division = divisions[init_data.division].name
        officer_birthday = init_data.birthday
        officers_degree = degree[init_data.degree].degree

        # self.ui.txtName.setText(officer_name)
        self.ui.lblName_5.setText(officer_name)
        # self.ui.txtName.setEnabled(False)
        self.ui.txtDivision.setText(officers_division)
        self.ui.txtDivision.setEnabled(False)
        self.ui.lblBDate.setText(officer_birthday)
        # self.ui.txtBDate.setEnabled(False)
        self.ui.txtDegree.setText(officers_degree)
        self.ui.txtDegree.setEnabled(False)

        # self.ui.cmbTasks.addItem('-')

        # for t in tasks.values():
        #     self.ui.cmbTasks.addItem(t.name, t)

        self.draw_line_chart()

    def draw_line_chart(self):
        series = QtCharts.QLineSeries()
        axis_x = QtCharts.QDateTimeAxis()
        first_date = {}
        count = []
        date = []
        time = []

        with create_session() as s:
            rows = fetch_task_results_by_user_id(s, self.officer_id)
            for r in rows:
                x = QDateTime.fromString(r.date, 'yyyy-MM-dd')
                count.append(r.count)
                time.append(r.time)
                date.append(r.date)
                if 1 not in first_date:
                    first_date[1] = x
                y = r.count
                series.append(float(x.toMSecsSinceEpoch()), y)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
        chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeDark)

        axis_x.setFormat("dd.MM.yyyy")
        # axis_x.setTickCount(10)
        axis_x.setMax(QtCore.QDateTime.currentDateTime().addDays(30))
        axis_x.setMin(first_date[1])
        axis_x.setTitleText("Дата")
        series.setName('Num 4')
        series.setPointsVisible(True)
        series.setMarkerSize(4)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        # axis_y.setTickCount(6)
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Попаданий")
        axis_y.setMax(5)
        axis_y.setMin(0)

        chart.setAxisX(axis_x, series)
        chart.setAxisY(axis_y, series)

        # chart.addAxis(axis_x, Qt.AlignBottom)
        # series.attachAxis(axis_x)
        self.model.set_count(count)
        self.model.set_date(date)
        self.model.set_time(time)

        self.ui.userChartView.setChart(chart)
