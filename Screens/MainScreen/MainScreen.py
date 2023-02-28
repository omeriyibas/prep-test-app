import os
import webbrowser

from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from Compenent.FileComp import FileComp
from Compenent.QuestionListComp import QuestionListComp
from MainScreen_design import Ui_MainWindow
from Screens.QuestionScreen.QuestionScreen import QuestionWindow
from Utils.PrintUtils import create_html
from Utils.QtUtils import clear_layout
from Utils.dbUtils import save_json, load_json
from Utils.fileUtils import get_file_name


class MainWindow(QMainWindow):

    # resized=pyqtSignal()

    def init_window(self):

        self.show()

        self.timer=QTimer()
        self.timer.timeout.connect(self.show_exam)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = load_json("db/settings.json")

        self.check_file()

        self.ui.label.setText(self.file_name)

        self.q_comp = QuestionListComp()
        self.q_comp.btn_signal.connect(self.open_question)

        self.file_comp = FileComp()

        self.q_window = QuestionWindow()
        self.q_window.add_signal.connect(self.add_question)
        self.q_window.update_signal.connect(self.update_question)

        self.init_ui()

    def show_exam(self):
        self.timer.stop()
        url = os.path.join(os.getcwd(),"form_template","cikti.html")
        webbrowser.open(url)


    def create_exam(self):
        create_html(self.file_name,self.test)
        self.timer.start(100)


    def open_question(self,sira):
        idx=sira-1
        self.q_window.update_window(self.test[idx],idx)

    def check_file(self):
        try:
            self.file_path = self.settings["last_loaded_file"]
            self.test = load_json(self.file_path)
            self.file_name = get_file_name(self.file_path)
        except:
            self.test = None
            self.file_name = "No File Found"
            clear_layout(self.ui.gridLayout)

    # def resizeEvent(self,event):
    #     self.resized.emit()

    def add_question(self, question):
        self.test.append(question)
        save_json(self.test, self.file_path)
        self.refresh_table()

    def update_question(self, idx,question):
        self.test[idx]=question
        save_json(self.test, self.file_path)
        self.refresh_table()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionLoad.triggered.connect(self.load_file)
        self.ui.actionnew.triggered.connect(self.new_file)

        self.ui.view_btn.clicked.connect(self.create_exam)

        self.ui.add_btn.clicked.connect(self.show_add_question)
        self.ui.label.setText(self.file_name)
        self.refresh_table()


    def refresh_table(self):

        clear_layout(self.ui.gridLayout)

        if self.test is not None:
            self.fill()
        else:
            clear_layout(self.ui.gridLayout)



    def load_file(self):
        self.file_comp.load_file(self)

        self.prep_test()

    def new_file(self):
        self.file_comp.new_file(self)
        self.prep_test()

    def prep_test(self):
        self.settings["last_loaded_file"] = self.file_path

        save_json(self.settings, "db/settings.json")

        print(self.file_name)

        self.ui.label.setText(self.file_name)
        self.refresh_table()

    def show_add_question(self):
        self.q_window.add_window()

    def fill(self):
        len_test = len(self.test)
        col = int(self.width() / 100)
        row=int(len_test/col)+1

        if len_test>0:
            sira=0
            for i in range(row):
                if sira == len_test:
                    break
                for j in range(col):
                    sira+=1
                    self.q_comp.add_btn(self.ui, sira, i, j)
                    if sira==len_test:
                        break
        else:
            clear_layout(self.ui.gridLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.init_window()
    app.exec_()
