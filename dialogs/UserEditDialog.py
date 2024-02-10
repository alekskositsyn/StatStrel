from dialogs.UserCreateDialog import UserCreatDialog


class UserEditDialog(UserCreatDialog):
    def __init__(self, divisions, init_data, *args, **kwargs):
        super().__init__(divisions, *args, **kwargs)
        self.ui.btnAdd.setText('Изменить')

        first_name = init_data.first_name
        middle_name = init_data.middle_name
        last_name = init_data.last_name
        group = divisions[init_data.group_id].name
        officer_birthday = init_data.birth_date
        # q_date = QtCore.QDate.fromString(officer_birthday, "yyyy-MM-dd")
        identity_number = init_data.identity_number
        is_operator = init_data.is_operator

        self.ui.txtFirstName.setText(first_name)
        self.ui.txtMiddleName.setText(middle_name)
        self.ui.txtLastName.setText(last_name)
        self.ui.cmbDivisions.setCurrentText(group)
        self.ui.dateEdit.setDate(officer_birthday)
        self.ui.txtIdentityNum.setText(identity_number)
        self.ui.RBIsOperator.setChecked(is_operator)
