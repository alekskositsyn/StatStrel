from PySide6.QtWidgets import QDialog

from settings_ui import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.ui.btnSave.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)
        print('show')
        self.show()

    # def get_data(self):
    #     is_operator = self.ui.RBIsOperator.isChecked()
    #     if is_operator:
    #         is_operator = 1
    #     else:
    #         is_operator = 0
    #     return {
    #         'first_name': self.ui.txtFirstName.text(),
    #         'middle_name': self.ui.txtMiddleName.text(),
    #         'last_name': self.ui.txtLastName.text(),
    #         'birth_date': self.ui.dateEdit.date().toPython(),
    #         'group_id': self.ui.cmbDivisions.currentData().id,
    #         'identity_number': self.ui.txtIdentityNum.text(),
    #         'is_operator': is_operator
    #
    #         # 'degree': self.ui.cmbDegree.currentData().id
    #     }
