import docx

from common.class_user import User


def parsing_docx(path):
    doc = docx.Document(path)
    table = doc.tables[0]
    user_list = []
    for r in range(3):
        user = User
        if r == 0:
            continue
        row = table.rows[r]
        string = ''
        for c in range(len(row.cells)):
            cell = row.cells[c]
            if c == 1:
                name = cell.text.split()
                user.first_name, user.last_name, user.middle_name = name
            elif c == 2:
                date = cell.text
                user.birth_date = date
            elif c == 3:
                identity_number = cell.text
                user.identity_number = identity_number
            elif c == 4:
                division = cell.text
                user.division = division
        user_list.append(user)
