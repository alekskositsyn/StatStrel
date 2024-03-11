from PySide6 import QtCore


class UserProfileTableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.count = []
        self.date = []
        self.time = []
        self.points = []
        self.results = []

    def set_count(self, count: list) -> None:
        self.beginResetModel()
        self.count = count
        self.endResetModel()

    def set_date(self, date: list) -> None:
        self.date = date

    def set_time(self, time: list) -> None:
        self.time = time

    def set_points(self, points: list) -> None:
        self.points = points

    def set_results(self, results: list) -> None:
        self.results = results

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.count)

    def columnCount(self, *args, **kwargs) -> int:
        return 6

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            date = self.date[index.row()]
            points = self.points[index.row()]
            count = self.count[index.row()]
            time = self.time[index.row()]
            result = self.results[index.row()]
            column = index.column()
            if column == 0:
                return index.row() + 1
            elif column == 1:
                return date
            elif column == 2:
                return count
            elif column == 3:
                return points
            elif column == 4:
                return time
            elif column == 5:
                return result

    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Id',
                    1: 'Дата',
                    2: 'Кол-во\nвыстрелов',
                    3: 'Попаданий',
                    4: 'Время',
                    5: 'Оценка',
                }.get(section)
