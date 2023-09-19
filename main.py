import sys

import PySide6
from sqlalchemy import create_engine, text
from PySide6.QtWidgets import QApplication, QMainWindow
from sqlalchemy.orm import Session

from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///database/db_statstrel.db", echo=True)
        self.insert_officer()
        self.load_officers()


    def load_officers(self):
        with Session(self.engine) as s:
            # query = """SELECT * FROM officers"""
            division_id = 2
            query = ''' 
            SELECT o.user, d.name
            FROM officers o
            JOIN main.divisions d
            on o.division = d.id
            where division = :d_id and degree = 3
            '''

            rows = s.execute(text(query), {"d_id": division_id})
            for r in rows:
                print(r)

    def insert_officer(self):
        with Session(self.engine) as s:
            query = '''
            insert into officers(user, birthday, division, degree)
            values (:user, :birthday, :division, :degree)
            '''
            s.execute(text(query), {
                "user": 'Туполев Алексей Геннадьевич',
                "birthday":'1992.12.01',
                "division": 4,
                "degree": 3
            })
            s.commit()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
