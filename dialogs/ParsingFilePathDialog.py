from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QProgressBar, QWidget, QVBoxLayout
from common.parsing_docx import parsing_docx
from dialogs.CheckParsFile import CheckParsFile
from user_interface.parsing_file_path_ui import Ui_ParsingFilePath


class ParsingFilePathDialog(QDialog):
    def __init__(self, divisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ParsingFilePath()
        self.ui.setupUi(self)
        self.divisions = divisions
        self.file_path = None
        self.users_list = None
        self.progress_bar = self.ui.progressBar

        self.ui.btn_cancle.clicked.connect(self.reject)
        self.ui.btn_save.clicked.connect(self.on_save_btn)
        self.ui.btn_check_file.clicked.connect(self.on_btn_check_file)
        self.ui.btn_path.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Microsoft Word (*.docx);;All Files (*)")
        if file_path:
            print("Выбран файл:", file_path)
            self.file_path = file_path

        self.ui.file_path_field.clear()
        self.ui.file_path_field.insert(file_path)

    def on_btn_check_file(self):
        remember_choice = QMessageBox()
        remember_choice.setWindowTitle("Внимание!!!")
        remember_choice.setText("Путь к файлу не выбран!")
        if not self.file_path:
            remember_choice.exec()
            return
        self.users_list = parsing_docx(self.file_path, self.progress_bar)

        dialog = CheckParsFile(self.users_list, self.divisions)
        r = dialog.exec()
        if r == 0:
            return

    def on_save_btn(self):
        print('Save')
        return self.accept()
