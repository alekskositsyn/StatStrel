from PySide6 import QtCore


class ListTableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.users_list = []
        self.divisions = {}
        self.degree = {}
        self.users_tests = {}

    def set_users(self, users_list):
        self.beginResetModel()
        self.users_list = users_list
        self.endResetModel()

    def set_degree(self, degree):
        self.degree = degree

    def set_divisions(self, divisions):
        self.divisions = divisions

    def set_users_tests(self, users_tests):
        self.users_tests = users_tests

    def rowCount(self, *args, **kwargs):
        # return super().rowCount(*args, **kwargs)
        return len(self.users_list)

    def columnCount(self, *args, **kwargs):
        return 7

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            user_info = self.users_list[index.row()]
            # degree = self.degree[user_info.degree].degree
            count_tests = self.users_tests[user_info.id]
            degree = self.degree[user_info.id]
            division = self.divisions[user_info.group_id].name
            column = index.column()
            if column == 0:
                return user_info.id
            elif column == 1:
                return user_info.last_name
            elif column == 2:
                return user_info.middle_name
            elif column == 3:
                return user_info.first_name
            elif column == 4:
                # if user_info.birth_date is None:
                #     return "Неизвестна"
                # return str(user_info.birth_date)
                return count_tests
            elif column == 5:
                return division
            elif column == 6:
                return degree
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.users_list[index.row()]

    def headerData(self, section, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Id',
                    1: 'Фамилия',
                    2: 'Имя',
                    3: 'Отчество',
                    4: 'Дата\nрождения',
                    5: 'Подразделение',
                    6: 'Уровень\nподготовки',
                }.get(section)
