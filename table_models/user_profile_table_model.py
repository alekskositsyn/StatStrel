from PySide6 import QtCore


class UserProfileTableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.count = []
        self.date = []
        self.time = []

    def set_count(self, count: list) -> None:
        self.beginResetModel()
        self.count = count
        self.endResetModel()
        print(count)

    def set_date(self, date: list) -> None:
        self.date = date

    def set_time(self, time: list) -> None:
        self.time = time

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.count)

    def columnCount(self, *args, **kwargs) -> int:
        return 4

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            date = self.date[index.row()]
            count = self.count[index.row()]
            time = self.time[index.row()]
            column = index.column()
            if column == 0:
                return index.row() + 1
            elif column == 1:
                return date
            elif column == 2:
                return count
            elif column == 3:
                return time



    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Id',
                    1: 'Дата',
                    2: 'Кол-во попаданий',
                    3: 'Время',
                }.get(section)
