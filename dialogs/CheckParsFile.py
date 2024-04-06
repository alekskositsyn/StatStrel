from PySide6 import QtCore
from PySide6.QtCore import QAbstractListModel
from PySide6.QtWidgets import QDialog

from user_interface.users_list_dialog_ui import Ui_UsersListDialog


class UserListModel(QAbstractListModel):
    def __init__(self, users=None):
        super().__init__()
        self.users = users or []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.users)

    def data(self, index, role):
        if not index.isValid() or not (0 <= index.row() < len(self.users)):
            return None

        user = self.users[index.row()]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            # Здесь вы можете выбрать, какую информацию отображать
            return f"{user.first_name} {user.last_name}"


class CheckParsFile(QDialog):
    def __init__(self, users, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_UsersListDialog()
        self.ui.setupUi(self)
        self.file_path = None
        self.users_list = users or []
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.accept)
        for row in self.users_list:
            self.ui.usersListWidget.addItem(
                f"{row.first_name} {row.middle_name} {row.last_name} "
                f"{row.identity_number} {row.birth_date} {row.group_id}"
            )
