from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

from Compenent.message import info_msg
from Screens.DescribeScreen.DescribeScreen import DescribeScreen
from Screens.QuestionScreen.QuestionScreen_design import Ui_MainWindow


class QuestionWindow(QMainWindow):
    add_signal = pyqtSignal(dict)
    update_signal = pyqtSignal(int,dict)

    def init_window(self):

        self.show()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.describe_window=DescribeScreen()
        # self.describe_window.description_signal.connect(self.get_description)


    def add_window(self):

        self.init_window()

        self.ui.describe_btn.setVisible(False)


        # self.description=""

        # self.ui.describe_btn.clicked.connect(lambda: self.describe_window.init_window(self.description))

        self.ui.save_btn.clicked.connect(self.save)

    def update_window(self, question,idx):

        self.question = question

        self.idx=idx

        self.init_window()

        self.ui.describe_btn.setVisible(False)

        # self.description=question["description"]

        # self.ui.describe_btn.clicked.connect(lambda: self.describe_window.update_window(self.description))



        self.fill_question()

        self.ui.save_btn.setText("UPDATE")
        self.ui.save_btn.clicked.connect(self.update)

    # def get_description(self,description):
    #     self.description=description

    def fill_question(self):
        self.ui.q_edt.setText(self.question["Q"])
        self.ui.a1_edt.setText(self.question["A1"])
        self.ui.a2_edt.setText(self.question["A2"])
        self.ui.a3_edt.setText(self.question["A3"])
        self.ui.a4_edt.setText(self.question["A4"])

        cb_list = [self.ui.cb1, self.ui.cb2, self.ui.cb3, self.ui.cb4]
        cb_list[self.question["Answer"]].setChecked(True)

    def update(self):
        self.get_question_form()

        self.update_signal.emit(self.idx,self.question)

        self.close()

    def get_question_form(self):
        self.question = {}
        self.question["Q"] = self.ui.q_edt.toPlainText()
        self.question["A1"] = self.ui.a1_edt.toPlainText()
        self.question["A2"] = self.ui.a2_edt.toPlainText()
        self.question["A3"] = self.ui.a3_edt.toPlainText()
        self.question["A4"] = self.ui.a4_edt.toPlainText()
        cb_list = [self.ui.cb1.isChecked(), self.ui.cb2.isChecked(), self.ui.cb3.isChecked(), self.ui.cb4.isChecked()]
        try:
            self.question["Answer"] = cb_list.index(True)
        except:
            info_msg(self, "please select answer")
            self.question=None

        # self.question["description"] = self.description


    def save(self):
        self.get_question_form()

        if self.question:
            self.add_signal.emit(self.question)

            self.close()


# if __name__ == '__main__':
#     app = QApplication([])
#     window = ()
#     window.init_window()
#     app.exec_()
