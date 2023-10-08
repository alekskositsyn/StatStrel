import sys

from sqlalchemy import create_engine, text
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from sqlalchemy.orm import Session
from PySide6 import QtCore
from mainwindow_ui import Ui_MainWindow
from add_officer_ui import Ui_Dialog


class EditDialog(QDialog):
    def __init__(self, degree, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        for r in degree.values():
            self.ui.cmbDegree.addItem(r.degree, r)
        for r in divisions.values():
            self.ui.cmbDivisions.addItem(r.name, r)

    def get_data(self):
        return {
            'name': self.ui.txtName.text(),
            'division': self.ui.cmbDivisions.currentData().id,
            'birthday': self.ui.dateEdit.date().toPython(),
            'degree': self.ui.cmbDegree.currentData().id
        }


class UpdateDialog(EditDialog):
    def __init__(self, degree, divisions, init_data, *args, **kwargs):
        super().__init__(degree, divisions, *args, **kwargs)
        self.ui.btnAdd.setText('Изменить')

        officer_name = init_data.user
        officers_division = divisions[init_data.division].name
        officer_birthday = init_data.birthday
        q_date = QtCore.QDate.fromString(officer_birthday, "yyyy-MM-dd")
        officers_degree = degree[init_data.degree].degree

        self.ui.txtName.setText(officer_name)
        self.ui.cmbDivisions.setCurrentText(officers_division)
        self.ui.dateEdit.setDate(q_date)
        self.ui.cmbDegree.setCurrentText(officers_degree)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.divisions = None
        self.degree = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///database/db_statstrel.db", echo=True)
        self.load_divisions()
        self.load_degree()
        self.load_officers()

        self.ui.cmb_division.currentIndexChanged.connect(self.load_officers)
        self.ui.cmb_degree.currentIndexChanged.connect(self.load_officers)
        self.ui.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.on_btn_remove_clicked)
        self.ui.btn_update.clicked.connect(self.on_btn_update_clicked)

    def on_btn_update_clicked(self):
        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Редактирование профиля сотрудника")
        remember_choice.setText("Выберите сотрудника для редактирования")
        item = self.ui.list_table.currentItem()
        if item is None:
            remember_choice.exec()
            return
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        print(data)

        dialog = UpdateDialog(self.degree, self.divisions, data)
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return

    def on_btn_add_clicked(self):
        """ Добавление нового сотрудника"""

        dialog = EditDialog(self.degree, self.divisions)
        r = dialog.exec()
        if r == 0:
            print('Exit')
            return

        data = dialog.get_data()
        with Session(self.engine) as s:
            query = '''
            insert into officers(user, birthday, division, degree)
            values (:user, :birthday, :division, :degree)
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
        item = self.ui.list_table.currentItem()
        if item is None:
            remember_choice.exec()
            return
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        item_id = data.id
        r = QMessageBox.question(self, "Подтверждение", "Точно ли хотите удалить")
        if r == QMessageBox.StandardButton.No:
            return
        with Session(self.engine) as s:
            query = """
                delete from officers
                where id = :id
            """

            s.execute(text(query), {"id": item_id})
            s.commit()
        self.load_officers()

    def load_officers(self):
        """ Вывод списка сотрудников """

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

        self.ui.list_table.clear()
        with Session(self.engine) as s:
            query = """
                select * from officers 
                where (:did = 0 or division = :did) 
                and (:d = 0 or degree = :d)
                order by user
                """

            rows = s.execute(text(query), {"did": division_id, "d": degree_id})
            for r in rows:
                degree_name = self.degree[r.degree].degree
                division_name = self.divisions[r.division].name
                item = QListWidgetItem(f'{r.id}: {r.user} {r.birthday} {degree_name} {division_name}')
                item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
                self.ui.list_table.addItem(item)

    def load_degree(self):
        """ Вывод списка уровня подготовки """

        self.ui.cmb_degree.addItem('-')

        with Session(self.engine) as s:
            self.degree = {}
            query = """select * from degree"""
            rows = s.execute(text(query))
            for r in rows:
                self.degree[r.id] = r
                self.ui.cmb_degree.addItem(r.degree, r)

    def load_divisions(self):
        """ Вывод списка подразделений """

        with Session(self.engine) as s:
            self.divisions = {}
            query = """select * from divisions"""
            rows = s.execute(text(query))
            for r in rows:
                self.divisions[r.id] = r

        self.ui.cmb_division.addItem('-')
        for division in self.divisions.values():
            self.ui.cmb_division.addItem(division.name, division)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
