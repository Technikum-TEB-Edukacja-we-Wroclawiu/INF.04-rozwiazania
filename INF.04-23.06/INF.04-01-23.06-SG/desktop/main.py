import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('okno.ui', self)

        self.button_check_price = self.findChild(QtWidgets.QPushButton, 'pushButton_check_price')
        self.button_check_price.clicked.connect(self.check_price)

        self.button_apply = self.findChild(QtWidgets.QPushButton, 'pushButton_apply')
        self.button_apply.clicked.connect(self.check_address)

        self.groupbox_type_of_parcel = self.findChild(QtWidgets.QButtonGroup, 'buttonGroup_parcel_type')

        self.input_street = self.findChild(QtWidgets.QLineEdit, 'lineEdit_street')
        self.input_postal_code = self.findChild(QtWidgets.QLineEdit, 'lineEdit_postal_code')
        self.input_city = self.findChild(QtWidgets.QLineEdit, 'lineEdit_city')

        self.label_img = self.findChild(QtWidgets.QLabel, 'label_img')
        self.label_price = self.findChild(QtWidgets.QLabel, 'label_price')

        self.show()

    def check_price(self):
        parcels = {
            -2: ["1 zł", "pocztowka.png"],  # pierwsze id to -2, potem idzie w dół
            -3: ["1,5 zł", "list.png"],
            -4: ["10 zł", "paczka.png"]
        }

        checked_parcel_type = self.groupbox_type_of_parcel.checkedId()
        self.label_price.setText(f"Cena: {parcels[checked_parcel_type][0]}")
        self.label_img.setPixmap(QPixmap(f"images/{parcels[checked_parcel_type][1]}"))

    def check_address(self):
        postal_code = self.input_postal_code.text()
        msg = "Dane przesyłki zostały wprowadzone"
        if len(postal_code) != 5:
            msg = "Nieprawidłowa liczba cyfr w kodzie pocztowym"
        elif not postal_code.isnumeric():
            msg = "Kod pocztowy powinien się składać z samych cyfr"

        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(msg)
        msgbox.setWindowTitle("Informacja")
        msgbox.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
