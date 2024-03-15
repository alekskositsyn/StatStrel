from PySide6.QtWidgets import QDialog, QFileDialog

from common.parsing_docx import parsing_docx
from user_interface.parsing_file_path_ui import Ui_ParsingFilePath


class AddUsersList(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.user = User
        self.ui = Ui_ParsingFilePath()
        self.ui.setupUi(self)

        self.ui.btn_cancle.clicked.connect(self.reject)
        self.ui.btn_check_file.clicked.connect(self.accept)
        self.ui.btn_path.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Microsoft Word (*.docx);;All Files (*)")
        if file_path:
            print("Выбран файл:", file_path)
        self.ui.file_path_field.clear()
        self.ui.file_path_field.insert(file_path)
        parsing_docx(file_path)
