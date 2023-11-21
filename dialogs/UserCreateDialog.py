from PySide6.QtWidgets import QDialog

from add_officer_ui import Ui_Dialog


class UserCreatDialog(QDialog):
    def __init__(self, degree, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        for r in degree.values():
            self.ui.cmbDegree.addItem(r.degree, r)
        for r in divisions.values():
            self.ui.cmbDivisions.addItem(r.name, r)

    def get_data(self):
        return {
            'name': self.ui.txtName.text(),
            'division': self.ui.cmbDivisions.currentData().id,
            'birthday': self.ui.dateEdit.date().toPython(),
            'degree': self.ui.cmbDegree.currentData().id
        }
