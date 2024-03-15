from PySide6.QtWidgets import QDialog
from common.class_user import User
from user_interface.add_officer_ui import Ui_dialog


class UserCreatDialog(QDialog):
    def __init__(self, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = User
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        for r in divisions.values():
            self.ui.cmbDivisions.addItem(r.name, r)

    def get_data(self):
        is_operator = self.ui.RBIsOperator.isChecked()
        personal_number = self.ui.txtIdentityNum.text()
        if not personal_number:
            personal_number = None
        if is_operator:
            is_operator = 1
        else:
            is_operator = 0
        self.user.first_name = self.ui.txtFirstName.text()
        self.user.last_name = self.ui.txtLastName.text()
        self.user.middle_name = self.ui.txtMiddleName.text()
        self.user.birth_date = self.ui.dateEdit.date().toPython()
        self.user.group_id = self.ui.cmbDivisions.currentData().id
        self.user.personal_number = personal_number
        self.user.is_operator = is_operator
        return self.user
