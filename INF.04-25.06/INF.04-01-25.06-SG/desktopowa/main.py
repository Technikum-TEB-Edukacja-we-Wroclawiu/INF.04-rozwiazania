import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from layout import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__r = 255
        self.__g = 255
        self.__b = 255

        self.slider_r.valueChanged.connect(self.update_rgb)
        self.slider_g.valueChanged.connect(self.update_rgb)
        self.slider_b.valueChanged.connect(self.update_rgb)

        self.btn_get_color.clicked.connect(self.update_rect_small)

    def update_rgb(self):
        self.__r = self.slider_r.value()
        self.__g = self.slider_g.value()
        self.__b = self.slider_b.value()

        self.lbl_r.setText(str(self.__r))
        self.lbl_g.setText(str(self.__g))
        self.lbl_b.setText(str(self.__b))

        self.rect_big.setStyleSheet(f"background-color: rgb({self.__r}, {self.__g}, {self.__b})")

    def update_rect_small(self):
        self.rect_small.setStyleSheet(f"background-color: rgb({self.__r}, {self.__g}, {self.__b})")
        self.rect_small.setText(f"{self.__r}, {self.__g}, {self.__b}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
