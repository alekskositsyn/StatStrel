import sys

import PySide6
from sqlalchemy import create_engine, text
from PySide6.QtWidgets import QApplication, QMainWindow
from sqlalchemy.orm import Session

from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.divisions = None
        self.degree = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///database/db_statstrel.db", echo=True)
        self.select_divisions()
        self.select_degree()
        self.load_officers()

        self.ui.cmb_division.currentIndexChanged.connect(self.load_officers)
        self.ui.cmb_degree.currentIndexChanged.connect(self.load_officers)

    def load_officers(self):
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
                degree_name = self.degree[r.id].degree
                division_name = self.divisions[r.id].name
                self.ui.list_table.addItem(f'{r.id}: {r.user} {r.birthday} {degree_name} {division_name}')

    def select_degree(self):
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

    def insert_officer(self):
        with Session(self.engine) as s:
            query = '''
            insert into officers(user, birthday, division, degree)
            values (:user, :birthday, :division, :degree)
            '''
            s.execute(text(query), {
                "user": 'Туполев Алексей Геннадьевич',
                "birthday": '1992.12.01',
                "division": 4,
                "degree": 3
            })
            s.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
