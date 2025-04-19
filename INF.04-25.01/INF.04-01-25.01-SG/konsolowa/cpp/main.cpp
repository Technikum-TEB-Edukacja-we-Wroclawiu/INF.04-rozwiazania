#include <iostream>
#include <random>
#include <numeric>

class ArrayOperations {
private:
    int *numbers;
    int size;

public:
    explicit ArrayOperations(const int size) {
        this->size = size;
        this->numbers = new int[size];

        std::default_random_engine generator;
        std::uniform_int_distribution<int> distribution(1, 1000);
        for (int i = 0; i < size; i++) {
            this->numbers[i] = distribution(generator);
        }
    }

    ~ArrayOperations() {
        delete[] this->numbers;
    }

    /**
     * nazwa metody: display
     * opis metody: metoda wyświetla wszystkie liczby w tablicy `numbers` w osobnych liniach
     * parametry: brak
     * zwracany typ i opis: brak
     * autor: 123456789112
     */
    void display() const {
        for (int i = 0; i < this->size; i++) {
            std::cout << this->numbers[i] << std::endl;
        }
    }

    [[nodiscard]] int findFirst(const int needle) const {
        for (int i = 0; i < this->size; i++) {
            if (this->numbers[i] == needle) {
                return i;
            }
        }
        return -1;
    }

    [[nodiscard]] int displayOdds() const {
        int counter = 0;
        for (int i = 0; i < this->size; i++) {
            if (this->numbers[i] % 2 == 1) {
                counter++;
                std::cout << this->numbers[i] << std::endl;
            }
        }

        return counter;
    }

    [[nodiscard]] double getMean() const {
        int total = std::accumulate(this->numbers, this->numbers + this->size, 0);
        return static_cast<double>(total) / static_cast<double>(this->size);
    }
};

int main() {
    auto arrayOps = ArrayOperations(21);

    std::cout << "Wszystkie elementy tablicy:" << std::endl;
    arrayOps.display();

    int index_42 = arrayOps.findFirst(42);
    if (index_42 != -1) {
        std::cout << "Liczbę 42 znaleziono na indeksie " << index_42 << "." << std::endl;
    }

    std::cout << "Liczby nieparzyste:" << std::endl;
    auto odds = arrayOps.displayOdds();
    std::cout << "Liczba liczb nieparzystych w tablicy: " << odds << "." << std::endl;

    std::cout << "Średnia wszystkich liczb w tablicy: " << arrayOps.getMean() << std::endl;

    return 0;
}
