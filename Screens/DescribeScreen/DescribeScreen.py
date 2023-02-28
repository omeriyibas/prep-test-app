from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from Screens.DescribeScreen.DescribeScreen_design import Ui_MainWindow

class DescribeScreen(QMainWindow):

    description_signal=pyqtSignal(str)

    def init_window(self,descripton):
        self.show()

        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.q_edt.setText(descripton)

        self.ui.save_btn.clicked.connect(self.send_description)

    def send_description(self):
        self.description_signal.emit(self.ui.q_edt.toPlainText())
        self.close()

    def update_window(self,descripton):
        self.init_window(descripton)
        self.ui.save_btn.setText("UPDATE")




# if __name__ == '__main__':
#     app=QApplication([])
#     window=()
#     window.init_window()
#     app.exec_()