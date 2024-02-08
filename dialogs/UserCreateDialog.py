from PySide6.QtWidgets import QDialog

from add_officer_ui import Ui_dialog


class UserCreatDialog(QDialog):
    def __init__(self, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        # for r in degree.values():
        #     self.ui.cmbDegree.addItem(r.degree, r)
        for r in divisions.values():
            self.ui.cmbDivisions.addItem(r.name, r)

    def get_data(self):
        return {
            'first_name': self.ui.txtFirstName.text(),
            'middle_name': self.ui.txtMiddleName.text(),
            'last_name': self.ui.txtLastName.text(),
            'birth_date': self.ui.dateEdit.date().toPython(),
            'group_id': self.ui.cmbDivisions.currentData().id,
            'identity_number': self.ui.txtIdentityNum.text(),
            'is_operator': self.ui.RBIsOperator.isChecked()

            # 'degree': self.ui.cmbDegree.currentData().id
        }
