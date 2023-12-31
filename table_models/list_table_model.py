from PySide6 import QtCore
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget





class ListTableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.users_list = []
        self.divisions = {}
        self.degree = {}

    def set_users(self, users_list):
        self.beginResetModel()
        self.users_list = users_list
        self.endResetModel()

    def set_degree(self, degree):
        self.degree = degree

    def set_divisions(self, divisions):
        self.divisions = divisions

    def rowCount(self, *args, **kwargs):
        # return super().rowCount(*args, **kwargs)
        return len(self.users_list)

    def columnCount(self, *args, **kwargs):
        return 5

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            user_info = self.users_list[index.row()]
            degree = self.degree[user_info.degree].degree
            division = self.divisions[user_info.division].name
            column = index.column()
            if column == 0:
                return user_info.id
            elif column == 1:
                return user_info.user
            elif column == 2:
                return user_info.birthday
            elif column == 3:
                return division
            elif column == 4:
                return degree
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.users_list[index.row()]

    def headerData(self, section, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Id',
                    1: 'ФИО',
                    2: 'Дата рождения',
                    3: 'Подразделение',
                    4: 'Уровень подготовки',
                }.get(section)
