from PySide6.QtWidgets import QDialog

from user_interface.add_officer_ui import Ui_dialog


class UserCreatDialog(QDialog):
    def __init__(self, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        return {
            'first_name': self.ui.txtFirstName.text(),
            'middle_name': self.ui.txtMiddleName.text(),
            'last_name': self.ui.txtLastName.text(),
            'birth_date': self.ui.dateEdit.date().toPython(),
            'group_id': self.ui.cmbDivisions.currentData().id,
            'personal_number': personal_number,
            'is_operator': is_operator
        }
