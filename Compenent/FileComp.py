import os

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog

from Utils.dbUtils import save_json, load_json


class FileComp(QObject):

    def new_file(self, window):
        if os.name == "nt":
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        else:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        window.file_path, _ = QFileDialog.getSaveFileName(window, "Select Folder",
                                                          desktop,
                                                          "(*.json)",
                                                          options=QFileDialog.DontUseNativeDialog)


        try:
            save_json([], f"{window.file_path}.json")
            window.test = load_json(f"{window.file_path}.json")
            window.file_name = window.file_path.split("/")[-1]
        except:
            pass

    def load_file(self, window):
        if os.name == "nt":
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        else:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        window.file_path, _ = QFileDialog.getOpenFileName(window, "Select Files",
                                                          desktop,
                                                          "(*.json)",
                                                          options=QFileDialog.DontUseNativeDialog)

        window.file_name = window.file_path.split("/")[-1].split(".")[0]

        try:
            window.test = load_json(window.file_path)
        except:
            pass
