import docx
from PySide6.QtWidgets import QApplication

from common.class_user import User
from dialogs.ProgressBarDialog import ProgressBarDialog


def parsing_docx(path, progress_bar):
    first_name: str = ''
    last_name: str = ''
    middle_name: str = ''
    birth_date: str = ''
    identity_number: str = ''
    division: str = ''
    doc = docx.Document(path)
    table = doc.tables[0]
    users_list = []
    progress_bar.show()
    # progress_bar.setVisible(True)
    progress_bar.setMaximum(len(table.rows)-1)
    for r in range(1, (len(table.rows))):
        if r == 0:
            continue
        row = table.rows[r]
        string = ''
        for c in range(len(row.cells)):
            cell = row.cells[c]
            if c == 1:
                name = cell.text.split()
                first_name, last_name, middle_name = name
            elif c == 2:
                birth_date = cell.text
            elif c == 3:
                identity_number = cell.text
            elif c == 4:
                division = cell.text
        user = User(first_name, last_name, middle_name, birth_date, identity_number, division)
        users_list.append(user)
        progress_bar.setValue(int(r * 100 / len(table.rows)))
        QApplication.processEvents()
    return users_list
