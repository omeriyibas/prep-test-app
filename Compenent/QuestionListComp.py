from PyQt5.QtCore import QObject, pyqtSignal, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class QuestionListComp(QObject):
    btn_signal=pyqtSignal(int)

    font = QFont()
    font.setFamily(u"aakar")
    font.setPointSize(20)

    def add_btn(self, ui, sira, i, j):
        ui.q_btn = QPushButton(ui.gridFrame)
        ui.q_btn.setObjectName(u"q_btn")

        ui.q_btn.setMinimumSize(QSize(70, 70))
        ui.q_btn.setMaximumSize(QSize(70, 70))
        ui.q_btn.setFont(self.font)
        ui.q_btn.setStyleSheet(u"QPushButton{\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius:15px;}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "background-color: rgb(85, 0, 255);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "border-radius:15px;}")

        ui.q_btn.setText(f"Q{sira}")

        ui.q_btn.clicked.connect(lambda: self.btn_signal.emit(sira))

        ui.gridLayout.addWidget(ui.q_btn, i, j, 1, 1)