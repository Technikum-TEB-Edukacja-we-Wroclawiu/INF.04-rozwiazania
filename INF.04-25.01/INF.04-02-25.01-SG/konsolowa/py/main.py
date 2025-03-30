class Device:
    @staticmethod
    def show_message(message: str) -> None:
        """
        ******************
        Nazwa: show_message
        Opis: metoda wyświetla w konsoli wiadomość podaną jako parametr.
        Parametry: message - wiadomość do wyświetlenia
        Zwracany typ i opis: brak
        Autor: 123456789112
        ******************
        """
        print(message)


class WashingMachine(Device):
    def __init__(self):
        self.__program = 0

    def set_program(self, program: int) -> int:
        if 1 <= program <= 12:
            self.__program = program
        else:
            self.__program = 0

        return self.__program


class VacuumCleaner(Device):
    def __init__(self):
        self.__status = False

    def on(self):
        if not self.__status:
            self.__status = True
            Device.show_message("Odkurzacz włączono")

    def off(self):
        if self.__status:
            self.__status = False
            Device.show_message("Odkurzacz wyłączono")


def main():
    vacuum = VacuumCleaner()
    washing_machine = WashingMachine()

    program = int(input("Podaj numer prania 1..12: "))
    if program == washing_machine.set_program(program):
        print("Program został ustawiony")
    else:
        print("Podano niepoprawny numer programu")

    vacuum.on()
    vacuum.on()
    vacuum.on()
    Device.show_message("Odkurzacz wyładował się")
    vacuum.off()


if __name__ == '__main__':
    main()
