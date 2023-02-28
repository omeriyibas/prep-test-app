from PyQt5.QtGui import QImage, QPixmap


def clear_layout(layout):
    for i in range(layout.count()):
        layout.itemAt(i).widget().deleteLater()

def convert_cv_qt(cv_img):
    h, w, ch = cv_img.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
    return QPixmap.fromImage(convert_to_Qt_format)