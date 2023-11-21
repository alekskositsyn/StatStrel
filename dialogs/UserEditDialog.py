from PySide6 import QtCore

from dialogs.UserCreateDialog import UserCreatDialog


class UserEditDialog(UserCreatDialog):
    def __init__(self, degree, divisions, init_data, *args, **kwargs):
        super().__init__(degree, divisions, *args, **kwargs)
        self.ui.btnAdd.setText('Изменить')

        officer_name = init_data.user
        officers_division = divisions[init_data.division].name
        officer_birthday = init_data.birthday
        q_date = QtCore.QDate.fromString(officer_birthday, "yyyy-MM-dd")
        officers_degree = degree[init_data.degree].degree

        self.ui.txtName.setText(officer_name)
        self.ui.cmbDivisions.setCurrentText(officers_division)
        self.ui.dateEdit.setDate(q_date)
        self.ui.cmbDegree.setCurrentText(officers_degree)
