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

    def load_officers(self):
        division_id = self.ui.cmb_division.currentData().id
        self.ui.list_table.clear()
        with Session(self.engine) as s:
            query = """SELECT * FROM officers where division = :did order by user"""

            rows = s.execute(text(query), {"did": division_id})
            for r in rows:
                degree_name = self.degree[r.id].degree
                division_name = self.divisions[r.id].name
                self.ui.list_table.addItem(f'{r.id}: {r.user} {r.birthday} {degree_name} {division_name}')

    def select_degree(self):
        with Session(self.engine) as s:
            self.degree = {}
            query = """select * from degree"""
            rows = s.execute(text(query))
            for r in rows:
                self.degree[r.id] = r

    def select_divisions(self):
        with Session(self.engine) as s:
            self.divisions = {}
            query = """select * from divisions"""
            rows = s.execute(text(query))
            for r in rows:
                self.divisions[r.id] = r
            print(self.divisions)

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
