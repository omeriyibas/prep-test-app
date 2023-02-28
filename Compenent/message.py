from PyQt5.QtWidgets import QMessageBox


def info_msg(window,message):
    QMessageBox.information(window, "", f"{message}")

def critical_msg(window,message):
        msg = QMessageBox.critical(window, "", f"{message}",
                                   QMessageBox.Yes | QMessageBox.No)
        return msg == QMessageBox.Yes