import datetime

from PySide6 import QtCharts, QtWidgets
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6 import QtCore

from common.handler_users_results import handler_users_results
from data.create_session import create_session, create_session_to_mysql
from data.insert_user_results import insert_user_results
from data.select_results_by_user_id import select_results_by_user_id
from table_models.user_profile_table_model import UserProfileTableModel
from user_interface.user_profile_ui import Ui_Dialog


class UserProfileDialog(QDialog):
    def __init__(self, divisions, init_data, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.config = config

        self.model = UserProfileTableModel()
        self.ui.table_user_profile.setModel(self.model)
        self.ui.table_user_profile.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents
        )
        self.ui.dateEdit.setDate(QDateTime.currentDateTime().date())

        self.user_id = init_data.id
        first_name = init_data.first_name
        middle_name = init_data.middle_name
        last_name = init_data.last_name
        officer_birthday = str(init_data.birth_date)
        group = divisions[init_data.group_id].name

        if officer_birthday == 'None':
            officer_birthday = 'Дата рождения\nне известна'

        self.ui.lblFirstName.setText(first_name)
        self.ui.lblMiddleName.setText(middle_name)
        self.ui.lblLastName.setText(last_name)
        # self.ui.txtName.setEnabled(False)
        self.ui.txtDivision.setText(group)
        self.ui.txtDivision.setEnabled(False)
        self.ui.lblBDate.setText(officer_birthday)
        self.ui.txtTime.setText('10')
        # self.ui.txtBDate.setEnabled(False)
        # self.ui.txtDegree.setText(officers_degree)
        # self.ui.txtDegree.setEnabled(False)
        self.ui.btnInsertData.clicked.connect(self.on_btn_insert_results)
        self.ui.txtPoints.textChanged.connect(self.set_count)

        # self.ui.cmbTasks.addItem('-')

        # for t in tasks.values():
        #     self.ui.cmbTasks.addItem(t.name, t)

        self.draw_line_chart()

    def set_count(self):
        points = self.ui.txtPoints.text()
        if points == '4':
            self.ui.txtCount.setText(points)

    def draw_line_chart(self):
        series = QtCharts.QLineSeries()
        axis_x = QtCharts.QDateTimeAxis()
        now_time = QDateTime.fromString(str(datetime.date.today()), 'yyyy-MM-dd')
        first_date = {}
        points = []
        count = []
        date = []
        time = []
        results = []

        with create_session_to_mysql(self.config) as s:
            rows = select_results_by_user_id(s, self.user_id)
            data = handler_users_results(rows)
            for r in data:
                x = QDateTime.fromString(str(r["date"].date()), 'yyyy-MM-dd')
                count.append(r["count"])
                points.append(r["points"])
                time.append(r["time"])
                date.append(x.date())
                results.append(r["result"])
                if 1 not in first_date:
                    first_date[1] = x
                y = r["points"]
                series.append(float(x.toMSecsSinceEpoch()), y)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
        chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeDark)

        axis_x.setFormat("dd.MM.yyyy")
        # axis_x.setTickCount(10)
        axis_x.setMax(QtCore.QDateTime.currentDateTime().addDays(30))
        if first_date:
            axis_x.setMin(first_date[1])
        else:
            first_date[2] = now_time
            axis_x.setMin(first_date[2])

        axis_x.setTitleText("Дата")
        series.setName('Статистика')
        series.setPointsVisible(True)
        series.setMarkerSize(4)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        # axis_y.setTickCount(6)
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Попаданий")
        axis_y.setMax(4)
        axis_y.setMin(0)

        chart.setAxisX(axis_x, series)
        chart.setAxisY(axis_y, series)

        # chart.addAxis(axis_x, Qt.AlignBottom)
        # series.attachAxis(axis_x)
        self.model.set_count(count)
        self.model.set_date(date)
        self.model.set_time(time)
        self.model.set_points(points)
        self.model.set_results(results)

        self.ui.userChartView.setChart(chart)

    def on_btn_insert_results(self):
        points = self.ui.txtPoints.text()
        count = self.ui.txtCount.text()
        time = self.ui.txtTime.text().replace(',', '.')
        date = self.ui.dateEdit.date()
        date = date.toString('yyyy-MM-dd')

        remember_choice = QMessageBox()
        remember_choice.setWindowTitle('Предупреждение')

        try:
            points = int(points)
            if points > 4:
                raise ValueError
        except ValueError:
            remember_choice.setText("Введите кол-во попаданий от 0 до 4")
            remember_choice.exec()
            return

        try:
            float(time)
            if 1 < float(time) > 10:
                raise ValueError
        except ValueError:
            remember_choice.setText("Введите время от 1 до 10")
            remember_choice.exec()
            return

        try:
            count = int(count)
            if count > 4:
                raise ValueError
        except ValueError:
            remember_choice.setText("Введите кол-во выстрелов от 0 до 4")
            remember_choice.exec()
            return

        if count < points:
            remember_choice.setText(
                "Количество выстрелов не может быть больше количества попаданий"
            )
            remember_choice.exec()
            return

        with create_session_to_mysql(self.config) as s:
            insert_user_results(s, self.user_id, points, count, time, date)

        self.ui.txtPoints.clear()
        self.ui.txtCount.clear()
        self.ui.txtTime.clear()

        self.draw_line_chart()
