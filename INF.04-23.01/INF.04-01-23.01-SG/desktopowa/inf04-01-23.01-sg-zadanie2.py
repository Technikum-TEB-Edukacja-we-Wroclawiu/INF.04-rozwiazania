import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QFormLayout, QCheckBox, QPushButton, QMessageBox


class AddEmployeeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.generated_password: str = ""
        self.initUI()

    def show_password_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setInformativeText(self.generated_password)
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.setWindowTitle("")
        messagebox.setFixedWidth(400)
        messagebox.exec()

    def not_enough_chars_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Błąd przy generowaniu hasła")
        messagebox.setInformativeText(
            f"Wprowadzona liczba znaków hasła jest zbyt mała, aby dodać do niej wybrane znaki. Odznacz część dodatkowych grup znaków.")
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.setWindowTitle("")
        messagebox.setFixedWidth(400)
        messagebox.exec()

    def apply_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setInformativeText(f"Dane pracownika: {self.name_input.text()} {self.surname_input.text()} {self.position_combo.currentText()} Hasło: {self.generated_password}")
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.setWindowTitle("")
        messagebox.setFixedWidth(400)
        messagebox.exec()

    def generate_password(self):
        password_length = int(self.character_number_input.text())
        include_lowercase_and_uppercase = self.lowercase_and_uppercase_chars_checkbox.isChecked()
        include_digits = self.digits_checkbox.isChecked()
        include_special_characters = self.special_characters_checkbox.isChecked()

        lowercase_character_set = "abcdefghijklmnopqrstuvwxyz"
        uppercase_character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits_character_set = "0123456789"
        special_characters_set = "!@#$%^&*()_+-="

        generated_password = ""
        for i in range(password_length):
            random_number = randint(0, len(lowercase_character_set) - 1)
            generated_password += lowercase_character_set[random_number]

        required_number_of_chars = 1 if include_lowercase_and_uppercase else 0
        required_number_of_chars += 1 if include_digits else 0
        required_number_of_chars += 1 if include_special_characters else 0

        if required_number_of_chars > password_length:
            self.not_enough_chars_messagebox()
        else:
            blocked_password_character_indexes = []
            if include_lowercase_and_uppercase:
                random_index = -1
                while random_index == -1 or random_index in blocked_password_character_indexes:
                    random_index = randint(0, len(generated_password) - 1)
                random_uppercase_char_index = randint(0, len(uppercase_character_set) - 1)

                generated_password = generated_password[:random_index] \
                                     + uppercase_character_set[random_uppercase_char_index] \
                                     + generated_password[random_index + 1:]
                blocked_password_character_indexes.append(random_index)

            if include_digits:
                random_index = -1
                while random_index == -1 or random_index in blocked_password_character_indexes:
                    random_index = randint(0, len(generated_password) - 1)
                random_digit_index = randint(0, len(digits_character_set) - 1)

                generated_password = generated_password[:random_index] \
                                     + digits_character_set[random_digit_index] \
                                     + generated_password[random_index + 1:]
                blocked_password_character_indexes.append(random_index)

            if include_special_characters:
                random_index = -1
                while random_index == -1 or random_index in blocked_password_character_indexes:
                    random_index = randint(0, len(generated_password) - 1)
                random_special_char_index = randint(0, len(digits_character_set) - 1)

                generated_password = generated_password[:random_index] \
                                     + special_characters_set[random_special_char_index] \
                                     + generated_password[random_index + 1:]
                blocked_password_character_indexes.append(random_index)

        self.generated_password = generated_password
        self.show_password_messagebox()

    def initUI(self):
        self.setWindowTitle("Dodaj pracownika xxxxxxxxxxx")
        self.setStyleSheet("background-color: LightSteelBlue")

        # Grupa "Dane pracownika"
        employee_data_group = QGroupBox("Dane pracownika")
        employee_data_layout = QFormLayout()

        # Pole tekstowe na imię
        name_label = QLabel("Imię")
        self.name_input = QLineEdit()

        # Pole tekstowe na nazwisko
        surname_label = QLabel("Nazwisko")
        self.surname_input = QLineEdit()

        # Lista wyboru stanowiska
        position_label = QLabel("Stanowisko")
        self.position_combo = QComboBox()
        self.position_combo.addItem("Kierownik")
        self.position_combo.addItem("Starszy programista")
        self.position_combo.addItem("Młodszy programista")
        self.position_combo.addItem("Tester")

        # Dodanie pól tekstowych na imię, nazwisko i listy wyboru stanowiska do grupy "Dane pracownika"
        employee_data_layout.addRow(name_label, self.name_input)
        employee_data_layout.addRow(surname_label, self.surname_input)
        employee_data_layout.addRow(position_label, self.position_combo)

        # Ustawienie wyglądu grupy "Dane pracownika"
        employee_data_group.setLayout(employee_data_layout)

        # ########################

        # Grupa "Generowanie hasła"
        password_group = QGroupBox("Generowanie hasła")
        password_layout = QVBoxLayout()

        # Pole tekstowe na liczbę znaków
        character_number_label = QLabel("Ile znaków?")
        self.character_number_input = QLineEdit()

        # Pola wyboru — małe i wielkie litery, cyfry, znaki specjalne
        self.lowercase_and_uppercase_chars_checkbox = QCheckBox("Małe i wielkie litery", self)
        self.lowercase_and_uppercase_chars_checkbox.setChecked(True)
        self.digits_checkbox = QCheckBox("Cyfry", self)
        self.special_characters_checkbox = QCheckBox("Znaki specjalne", self)

        # Przycisk "Generuj hasło"
        generate_password_button = QPushButton("Generuj hasło", self)
        generate_password_button.setStyleSheet("background-color: SteelBlue; color: white")
        generate_password_button.setFixedWidth(100)
        generate_password_button.clicked.connect(self.generate_password)

        # Dodanie pola na liczbę znaków do grupy kontrolek "Generowanie hasła"
        character_number_hbox = QHBoxLayout()
        character_number_hbox.addWidget(character_number_label)
        character_number_hbox.addWidget(self.character_number_input)
        password_layout.addLayout(character_number_hbox)

        # Dodanie do grupy kontrolek "Generowanie hasła" checkboxów
        password_layout.addWidget(self.lowercase_and_uppercase_chars_checkbox)
        password_layout.addWidget(self.digits_checkbox)
        password_layout.addWidget(self.special_characters_checkbox)

        # Dodanie do grupy kontrolek "Generowanie hasła" przycisku na środku grupy
        password_button_hbox = QHBoxLayout()
        password_button_hbox.addStretch(1)
        password_button_hbox.addWidget(generate_password_button)
        password_button_hbox.addStretch(1)
        password_layout.addLayout(password_button_hbox)

        # Ustawienie wyglądu grupy na szczegóły hasła
        password_group.setLayout(password_layout)

        # Układ grup kontrolek "Dane pracownika" i "Generowanie hasła"
        data_groups_layout = QHBoxLayout()
        data_groups_layout.addWidget(employee_data_group)
        data_groups_layout.addWidget(password_group)

        # Układ na wyśrodkowany przycisk "Zatwierdź"
        apply_button_hbox = QHBoxLayout()
        apply_button = QPushButton("Zatwierdź", self)
        apply_button.setStyleSheet("background-color: SteelBlue; color: white")
        apply_button.setFixedWidth(200)
        apply_button.clicked.connect(self.apply_messagebox)
        apply_button_hbox.addStretch(1)
        apply_button_hbox.addWidget(apply_button)
        apply_button_hbox.addStretch(1)

        # Układ główny
        main_layout = QVBoxLayout()
        main_layout.addLayout(data_groups_layout)
        main_layout.addLayout(apply_button_hbox)

        self.setLayout(main_layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddEmployeeWindow()
    sys.exit(app.exec_())
