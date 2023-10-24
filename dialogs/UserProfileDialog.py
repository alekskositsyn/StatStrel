from PySide6 import QtCore

from PySide6.QtWidgets import QDialog

from user_profile_ui import Ui_Dialog


class UserProfileDialog(QDialog):
    def __init__(self, degree, divisions, init_data, tasks, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        officer_name = init_data.user
        officers_division = divisions[init_data.division].name
        officer_birthday = init_data.birthday
        officers_degree = degree[init_data.degree].degree

        self.ui.txtName.setText(officer_name)
        self.ui.txtDivision.setText(officers_division)
        self.ui.txtBDate.setText(officer_birthday)
        self.ui.txtDegree.setText(officers_degree)

        for t in tasks.values():
            self.ui.cmbTasks.addItem(t.name, t)

