import random
from typing import Optional


def create_filled_array(number_of_elements: int = 50) -> list:
    arr = []
    for _ in range(number_of_elements):
        arr.append(random.randint(1, 100))
    return arr


"""
**********************************************
Nazwa funkcji: find_element
Argumenty:     haystack - lista (tablica) wartości, wśród których należy
                          znaleźć daną wartość
               needle - wartość do znalezienia     
Typ zwracany:  int lub None, jeśli element znaleziono, jest zwracany
               indeks pierwszego wystąpienia elementu na liście,
               jeśli elementu nie ma - zwracane jest None.
Informacje:    Zaimplementowany algorytm to przeszukiwanie tablicy
               z wartownikiem. Nazwy parametrów funkcji pochodzą 
               od powiedzenia "szukanie igły w stogu siana" (ang. haystack 
               - stóg siana, needle - igła).
Autor:         961009xxxxx
**********************************************
"""
def find_element(haystack: list, needle: int) -> Optional[int]:
    haystack_copy = haystack.copy()
    haystack_copy.append(needle)
    watcher_index = len(haystack_copy) - 1
    for i in range(len(haystack_copy)):
        if haystack_copy[i] == needle and i != watcher_index:
            return i

    return None


if __name__ == '__main__':
    array_of_elements = create_filled_array(50)
    element_to_find = int(input("Wprowadź element do wyszukania: "))
    element_position = find_element(array_of_elements, element_to_find)
    print("Przeszukiwana tablica: ")
    print(array_of_elements)
    if element_position is None:
        print("Szukanego elementu nie ma w tej tablicy.")
    else:
        print(f"Szukany element znajduje się w tablicy po raz pierwszy na pozycji {element_position}.")
