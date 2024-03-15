import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore, QtWidgets

from common.config_load import load_config, save_config_file
from common.get_user_degree import get_user_degree
from common.handler_users_results import handler_users_results
from data.create_session import create_session_to_mysql
from data.delete_user import delete_user
from data.select_all_groups import select_all_groups
from data.select_results_by_user_id import select_results_by_user_id
from data.select_users import select_users
from data.insert_user import insert_user
from data.select_users_by_search import select_users_by_search
from data.update_user import update_user
from dialogs.AddUsersList import AddUsersList
from dialogs.DivisionChartDialog import DivisionChart
from dialogs.UserCreateDialog import UserCreatDialog
from dialogs.UserEditDialog import UserEditDialog
from dialogs.UserProfileDialog import UserProfileDialog
from dialogs.SettingsDialog import SettingsDialog
from table_models.list_table_model import ListTableModel
from user_interface.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.chart_view = None
        self.tasks = None
        self.divisions = None
        self.users_count_tests = {}
        self.users_degree = {}
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

        self.ui.tblItems.setModel(self.model)
        self.ui.tblItems.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tblItems.doubleClicked.connect(self.on_btn_profile_clicked)

        self.ui.cmb_division.currentIndexChanged.connect(self.load_users)
        self.ui.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.on_btn_remove_clicked)
        self.ui.btn_update.clicked.connect(self.on_btn_edit_clicked)
        self.ui.btn_profile.clicked.connect(self.on_btn_profile_clicked)
        self.ui.btnSearch.clicked.connect(self.search_user)
        self.ui.btn_settings_2.triggered.connect(self.on_btn_settings)
        self.ui.add_users_from_file.triggered.connect(self.on_btn_add_from_file)
        self.ui.btn_dev_degree.clicked.connect(self.show_div_chart)

    def on_btn_add_from_file(self):
        dialog = AddUsersList()
        r = dialog.exec()
        if r == 0:
            return

    def on_btn_settings(self):
        """ Вызов окна настроек подключения к БД """

        dialog = SettingsDialog()
        r = dialog.exec()
        if r == 0:
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

        with create_session_to_mysql(self.config) as s:
            rows = select_users(s, division_id)
            for r in rows:
                users_list.append(r)
                data = select_results_by_user_id(s, r.id)
                all_user_results = handler_users_results(data)
                self.users_count_tests[r.id] = (len(all_user_results))
                degree = get_user_degree(all_user_results)
                self.users_degree[r.id] = degree

        self.model.set_users(users_list)
        self.model.set_degree(self.users_degree)
        self.model.set_users_tests(self.users_count_tests)

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

    def show_div_chart(self):
        self.chart_view = DivisionChart(self.divisions, self.config)
        self.chart_view.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
