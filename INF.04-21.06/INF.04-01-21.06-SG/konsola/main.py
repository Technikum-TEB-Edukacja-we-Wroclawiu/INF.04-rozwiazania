class Sort:
    def __init__(self):
        self.array: list = []

    """
    /*************************************************************************
     * nazwa funkcji:       sort
     * parametry wejściowe: brak - funkcja (metoda) działa na polu klasy
     * wartość zwracana:    brak - funkcja (metoda) sortuje listę (tablicę)
                            przechowywaną jako pole klasy
     * autor:               961009xxxxx
     * ***********************************************************************/
    """
    def sort(self):
        for i in range(len(self.array)):
            max_index = self.__max(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

    """
    /*************************************************************************
     * nazwa funkcji:       __max
     * parametry wejściowe: range_start - początek zakresu listy do przeszukania
                            range_stop - koniec zakresu listy do przeszukania
                            jeśli te wartości nie zostaną podane, zostanie przeszukana
                            cała lista self.array będąca polem klasy
     * wartość zwracana:    int - indeks najwyższej wartości w podanym zakresie
       autor:               961009xxxxx
     * ***********************************************************************/
    """
    def __max(self, range_start: int = None, range_stop: int = None) -> int:
        if range_start is None:
            range_start = 0
        if range_stop is None:
            range_stop = len(self.array)

        greatest_index = None
        for i in range(range_start, range_stop):
            if greatest_index is None or self.array[i] > self.array[greatest_index]:
                greatest_index = i

        return greatest_index


if __name__ == '__main__':
    sort = Sort()
    print("Wprowadzanie wartości do tablicy")
    for i in range(10):
        tmp_value = int(input(f"Wprowadź wartość: {i + 1}: "))
        sort.array.append(tmp_value)

    print("Wprowadzona tablica:")
    print(sort.array)

    sort.sort()

    print("Posortowana tablica:")
    print(sort.array)
