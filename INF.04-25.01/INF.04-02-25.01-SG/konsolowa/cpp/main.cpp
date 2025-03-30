#include <iostream>

class Device {
public:
    /* ******************
     * Nazwa: showMessage
     * Opis: metoda wyświetla w konsoli wiadomość podaną jako parametr.
     * Parametry: message - wiadomość do wyświetlenia
     * Zwracany typ i opis: brak
     * Autor: 123456789112
     * ******************
     */
    static void showMessage(const std::string &message) {
        std::cout << message << std::endl;
    }
};

class WashingMachine : public Device {
private:
    int washingProgram = 0;

public:
    int setWashingProgram(const int washingProgram) {
        if (washingProgram >= 1 && washingProgram <= 12) {
            this->washingProgram = washingProgram;
        } else {
            this->washingProgram = 0;
        }
        return this->washingProgram;
    }
};

class VacuumCleaner : public Device {
private:
    bool status = false;

public:
    void on() {
        if (this->status == false) {
            this->status = true;
            Device::showMessage("Odkurzacz włączono");
        }
    }

    void off() {
        if (this->status == true) {
            this->status = false;
            Device::showMessage("Odkurzacz wyłączono");
        }
    }
};

int main() {
    auto vacuum = VacuumCleaner();
    auto washingMachine = WashingMachine();

    int washingProgram;
    std::cout << "Podaj numer prania 1..12: ";
    std::cin >> washingProgram;

    if (washingProgram == washingMachine.setWashingProgram(washingProgram)) {
        std::cout << "Program został ustawiony" << std::endl;
    } else {
        std::cout << "Podano niepoprawny numer programu" << std::endl;
    }

    vacuum.on();
    vacuum.on();
    vacuum.on();
    Device::showMessage("Odkurzacz wyładował się");
    vacuum.off();

    return 0;
}
