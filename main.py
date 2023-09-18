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

        self.load_officers()

    def load_officers(self):
        with Session(self.engine) as s:
            query = """
            SELECT * 
            FROM officers
            """

            rows = s.execute(text(query))
            for r in rows:
                print(r)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
