import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore, QtWidgets, QtCharts

from common.calc_mid_divisions import calc_mid_divisions
from common.config_load import load_config, save_config_file
from data.create_session import create_session, create_session_to_mysql
from data.delete_user import delete_user
from data.select_all_groups import select_all_groups
from data.select_users import select_users
from data.insert_user import insert_user
from data.select_users_by_search import select_users_by_search
from data.update_user import update_user
from dialogs.UserCreateDialog import UserCreatDialog
from dialogs.UserEditDialog import UserEditDialog
from dialogs.UserProfileDialog import UserProfileDialog
from dialogs.SettingsDialog import SettingsDialog
from table_models.list_table_model import ListTableModel
from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tasks = None
        self.divisions = None
        self.degree = None
        self.flag = True
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.config = load_config()
        self.model = ListTableModel()

        if not self.config:
            self.flag = False
            self.on_btn_settings()

        if self.flag:
            self.load_groups()
            self.load_users()
            # self.load_tasks()
            # self.load_degree()

        self.ui.tblItems.setModel(self.model)
        self.ui.tblItems.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tblItems.doubleClicked.connect(self.on_btn_profile_clicked)

        self.ui.cmb_division.currentIndexChanged.connect(self.load_users)
        # self.ui.cmb_degree.currentIndexChanged.connect(self.load_users)
        self.ui.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.on_btn_remove_clicked)
        self.ui.btn_update.clicked.connect(self.on_btn_edit_clicked)
        self.ui.btn_profile.clicked.connect(self.on_btn_profile_clicked)
        self.ui.btnSearch.clicked.connect(self.search_user)
        self.ui.btn_settings_2.triggered.connect(self.on_btn_settings)

    def on_btn_settings(self):
        """ Вызов окна настроек подключения к БД """

        dialog = SettingsDialog()
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return
        data = dialog.get_data()
        save_config_file(data)
        self.flag = True
        self.load_groups()
        self.load_users()

    def search_user(self):
        """ Поиск сотрудника """
        users_list = []
        line_search = self.ui.lineSearch
        params = line_search.text().strip()
        with create_session_to_mysql(self.config) as s:
            rows = select_users_by_search(s, params)
            for r in rows:
                users_list.append(r)
        # print(f'Searching user...{params}')
        self.model.set_users(users_list)
        line_search.clear()

    def on_btn_profile_clicked(self):
        """  Профиль сотрудника """

        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Профиль сотрудника")
        remember_choice.setText("Выберите сотрудника")

        item = self.ui.tblItems.currentIndex()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        if init_data is None:
            remember_choice.exec()
            return

        dialog = UserProfileDialog(self.divisions, init_data, self.config)
        dialog.exec()

    def on_btn_edit_clicked(self):
        """ Вызов окна редактирования данных сотрудника """

        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Редактирование данных сотрудника")
        remember_choice.setText("Выберите сотрудника для редактирования")
        item = self.ui.tblItems.currentIndex()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        if init_data is None:
            remember_choice.exec()
            return

        dialog = UserEditDialog(self.divisions, init_data)
        dialog.setWindowTitle("Редактирование данных сотрудника")
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return
        user_id = init_data.id
        data = dialog.get_data()

        with create_session_to_mysql(self.config) as s:
            update_user(s, user_id, data)
        self.load_users()

    def on_btn_add_clicked(self):
        """ Вызов окна добавления нового сотрудника """

        dialog = UserCreatDialog(self.divisions)
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return

        data = dialog.get_data()
        with create_session_to_mysql(self.config) as s:
            insert_user(s, data)
        self.load_users()

    def on_btn_remove_clicked(self):
        """ Удаление сотрудника """

        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Удаление")
        remember_choice.setText("Выберите сотрудника для удаления")
        item = self.ui.tblItems.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        if data is None:
            remember_choice.exec()
            return
        item_id = data.id
        r = QMessageBox.question(self, "Подтверждение", "Точно ли хотите удалить")
        if r == QMessageBox.StandardButton.No:
            return
        with create_session_to_mysql(self.config) as s:
            delete_user(s, item_id)
        self.load_users()

    def load_users(self):
        """ Вывод списка сотрудников """

        users_list = []
        divisions_data = self.ui.cmb_division.currentData()
        if divisions_data:
            division_id = self.ui.cmb_division.currentData().id
        else:
            division_id = 0

        # degree_data = self.ui.cmb_degree.currentData()
        # if degree_data:
        #     degree_id = self.ui.cmb_degree.currentData().id
        # else:
        #     degree_id = 0

        with create_session_to_mysql(self.config) as s:
            rows = select_users(s, division_id)
            for r in rows:
                users_list.append(r)

        self.model.set_users(users_list)
        # self.draw_divisions_bar_chart()

    # def load_degree(self):
    #     """ Вывод списка уровня подготовки """
    #     self.ui.cmb_degree.addItem('-')
    #     with create_session() as s:
    #         self.degree = {}
    #         rows = fetch_all_degree(s)
    #         for r in rows:
    #             self.degree[r.id] = r
    #             self.ui.cmb_degree.addItem(r.degree, r)
        # self.model.set_degree(self.degree)

    def load_groups(self):
        """ Вывод списка подразделений """

        self.ui.cmb_division.addItem('-')
        with create_session_to_mysql(self.config) as s:
            self.divisions = {}
            rows = select_all_groups(s)
            for r in rows:
                self.divisions[r.id] = r
        self.model.set_divisions(self.divisions)

        for division in self.divisions.values():
            self.ui.cmb_division.addItem(division.name, division)

    # def load_tasks(self):
    #     self.ui.cmbTasks.addItem('-')
    #     with create_session() as s:
    #         self.tasks = {}
    #         rows = fetch_all_tasks(s)
    #         for r in rows:
    #             self.tasks[r.id] = r
    #             self.ui.cmbTasks.addItem(r.name, r)

    # for task in self.tasks.values():
    #     self.ui.cmbTasks.addItem(task.name, task)

    def draw_divisions_bar_chart(self):
        chart = QtCharts.QChart()
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)

        series = QtCharts.QBarSeries()
        series.setName('Результаты подразделений')
        series.setLabelsVisible()
        series.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideEnd)

        bar_set = QtCharts.QBarSet("Результаты подразделений")
        bar_set.setColor("#3e3e3e")
        # bar_set.setLabelColor('#3e3e3e')

        divisions_names = []

        # for division in self.divisions.values():
        #     divisions_names.append(division.name)
        #     with create_session() as s:
        #         rows = fetch_task_4(s, division.id)
        #         result = calc_mid_divisions(rows)
        #
        #     bar_set.append(result)
        #     # Цвет результата на столбце
        #     # bar_set.setLabelColor('#3e3e3e')
        #     # Цвет столбца
        #     # bar_set.setColor("#3e3e3e")
        #     # Позиция результата на столбце
        # series.append(bar_set)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
