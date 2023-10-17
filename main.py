import sys

from PySide6.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import create_engine, text
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from sqlalchemy.orm import Session
from PySide6 import QtCore, QtWidgets

from data.create_session import create_session
from data.fetch_users import fetch_users
from dialogs.UserCreateDialog import UserCreatDialog
from dialogs.UserEditDialog import UserEditDialog
from table_models.list_table_model import ListTableModel
from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.divisions = None
        self.degree = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = ListTableModel()
        self.ui.tblItems.setModel(self.model)
        self.ui.tblItems.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.load_divisions()
        self.load_degree()
        self.load_officers()

        self.ui.cmb_division.currentIndexChanged.connect(self.load_officers)
        self.ui.cmb_degree.currentIndexChanged.connect(self.load_officers)
        self.ui.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.on_btn_remove_clicked)
        self.ui.btn_update.clicked.connect(self.on_btn_edit_clicked)

    def on_btn_edit_clicked(self):
        """  Редактирование данных сотрудника """

        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Редактирование данных сотрудника")
        remember_choice.setText("Выберите сотрудника для редактирования")
        item = self.ui.tblItems.currentIndex()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        if init_data is None:
            remember_choice.exec()
            return

        dialog = UserEditDialog(self.degree, self.divisions, init_data)
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return
        data = dialog.get_data()
        with create_session() as s:
            query = '''
                        UPDATE officers
                        SET user = :user, 
                            birthday = :birthday,
                            division = :division, 
                            degree = :degree
                        WHERE id = :id
                        '''
            s.execute(text(query), {
                "id": init_data.id,
                "user": data["name"],
                "birthday": data["birthday"],
                "division": data["division"],
                "degree": data["degree"]
            })
            s.commit()

        self.load_officers()

    def on_btn_add_clicked(self):
        """ Добавление нового сотрудника"""

        dialog = UserCreatDialog(self.degree, self.divisions)
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return

        data = dialog.get_data()
        with create_session() as s:
            query = '''
            INSERT INTO officers(user, birthday, division, degree)
            VALUES (:user, :birthday, :division, :degree)
            '''
            s.execute(text(query), {
                "user": data["name"],
                "birthday": data["birthday"],
                "division": data["division"],
                "degree": data["degree"]
            })
            s.commit()

        self.load_officers()

    def on_btn_remove_clicked(self):
        """ Удаление сотрудника """
        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Удаление")
        remember_choice.setText("Выберите сотрудника для удаления")
        item = self.ui.tblItems.currentIndex()
        if item is None:
            remember_choice.exec()
            return
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        item_id = data.id
        r = QMessageBox.question(self, "Подтверждение", "Точно ли хотите удалить")
        if r == QMessageBox.StandardButton.No:
            return
        with create_session() as s:
            query = """
                DELETE FROM officers
                WHERE id = :id
            """

            s.execute(text(query), {"id": item_id})
            s.commit()

        self.load_officers()

    def load_officers(self):
        """ Вывод списка сотрудников """
        users_list = []
        divisions_data = self.ui.cmb_division.currentData()
        if divisions_data:
            division_id = self.ui.cmb_division.currentData().id
        else:
            division_id = 0

        degree_data = self.ui.cmb_degree.currentData()
        if degree_data:
            degree_id = self.ui.cmb_degree.currentData().id
        else:
            degree_id = 0

        with create_session() as s:
            rows = fetch_users(s, division_id, degree_id)
            for r in rows:
                users_list.append(r)

        self.model.set_users(users_list)

    def load_degree(self):
        """ Вывод списка уровня подготовки """

        self.ui.cmb_degree.addItem('-')

        with create_session() as s:
            self.degree = {}
            query = """SELECT * FROM degree"""
            rows = s.execute(text(query))
            for r in rows:
                self.degree[r.id] = r
                self.ui.cmb_degree.addItem(r.degree, r)

        self.model.set_degree(self.degree)

    def load_divisions(self):
        """ Вывод списка подразделений """

        with create_session() as s:
            self.divisions = {}
            query = """SELECT * FROM divisions"""
            rows = s.execute(text(query))
            for r in rows:
                self.divisions[r.id] = r

        self.model.set_divisions(self.divisions)

        self.ui.cmb_division.addItem('-')
        for division in self.divisions.values():
            self.ui.cmb_division.addItem(division.name, division)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
