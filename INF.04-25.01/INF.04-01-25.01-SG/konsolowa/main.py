import random


class ArrayOperations:
    def __init__(self, num_elements: int):
        self.__num_elements: int = num_elements
        self.__numbers: list[int] = [random.randint(1, 1000) for _ in range(num_elements)]

    def print_elements(self) -> None:
        for i in range(self.__num_elements):
            print(f"{i}: {self.__numbers[i]}")

    def find_first(self, element: int) -> int:
        for i in range(self.__num_elements):
            if self.__numbers[i] == element:
                return i

        return -1

    def print_odd(self) -> int:
        num_odds = 0
        for num in self.__numbers:
            if num % 2 == 1:
                num_odds += 1
                print(num)

        return num_odds

    def avg(self) -> float:
        """
        ******
        Nazwa metody: avg
        Opis metody: oblicza średnią arytmetyczną elementów zapisanych w wewnętrznej tablicy `__numbers`
        Parametry: brak
        Zwracany typ i opis: float - średnia arytmetyczna
        Autor: 123456789112
        ******
        """
        return sum(self.__numbers) / self.__num_elements


def main():
    array_ops = ArrayOperations(21)
    array_ops.print_elements()

    find_idx = array_ops.find_first(42)
    if find_idx != -1:
        print(f"Wartość 42 znaleziono na indeksie {find_idx}")

    num_odds = array_ops.print_odd()
    print(f"Liczba elementów nieparzystych: {num_odds}")

    print(f"Średnia arytmetyczna wszystkich elementów: {array_ops.avg()}")



if __name__ == "__main__":
    main()
