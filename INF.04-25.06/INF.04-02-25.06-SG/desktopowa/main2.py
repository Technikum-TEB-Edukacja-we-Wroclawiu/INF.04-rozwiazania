import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from layout2 import Ui_MainWindow


class Caesar:
    @staticmethod
    def cipher(cleartext: str, key: int) -> str:
        if key == 0:
            return cleartext

        key = key % 26

        encrypted = ""

        for char in cleartext:
            if char not in "qwertyuiopasdfghjklzxcvbnm":
                encrypted += char
            else:
                new_char = ord(char) + key
                if new_char > ord('z'):
                    new_char -= 26
                encrypted += chr(new_char)

        return encrypted


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__cipher = ""

        self.btn_cipher.clicked.connect(self.handle_cipher)
        self.btn_save_to_file.clicked.connect(self.handle_save)

    def handle_cipher(self):
        cleartext = self.input_cleartext.toPlainText()
        tmp_key = self.input_key.toPlainText()
        key = 0
        try:
            key = int(tmp_key)
        except ValueError:
            pass

        self.__cipher = Caesar.cipher(cleartext, key)
        self.output_encrypted.setText(self.__cipher)

    def handle_save(self):
        file_name = QFileDialog.getSaveFileName(self, "Zapisz szyfr do pliku")
        print(f"{file_name=}", file=sys.stderr)

        if file_name[0] == '':
            return

        with open(file_name[0], "w", encoding="utf8") as f:
            f.write(self.__cipher)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
