from PySide6.QtWidgets import QDialog

from data.create_session import test_session_mysql
from settings_ui import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnSave.setEnabled(False)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnTestConn.clicked.connect(self.test_connection)
        self.ui.radioBtnOk.setText('')

    def get_data(self) -> dict:
        data = {
            'default_port': self.ui.txtPort.text(),
            'address': self.ui.txtAddress.text(),
            'database_name': self.ui.txtNameDB.text(),
            'database_pass': self.ui.txtPass.text(),
            'database_user': self.ui.txtUsername.text(),
        }
        return data

    def test_connection(self):
        config = self.get_data()

        if not test_session_mysql(config):
            self.ui.radioBtnOk.setText('No')
            return False

        self.ui.radioBtnOk.setCheckable(True)
        self.ui.radioBtnOk.setChecked(True)
        self.ui.radioBtnOk.setText('Ok')
        self.ui.btnSave.setEnabled(True)
