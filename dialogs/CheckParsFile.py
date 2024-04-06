from PySide6.QtWidgets import QDialog
from user_interface.users_list_dialog_ui import Ui_UsersListDialog


class CheckParsFile(QDialog):
    def __init__(self, users, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_UsersListDialog()
        self.ui.setupUi(self)
        self.file_path = None
        self.users_list = users or []
        self.divisions = divisions or []
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.accept)
        for row in self.users_list:
            self.ui.usersListWidget.addItem(
                f"{row.first_name} {row.middle_name} {row.last_name} "
                f"{row.identity_number} {row.birth_date} {self.divisions[int(row.group_id)].name}"
            )
