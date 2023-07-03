import math

"""
*********************************************************
  nazwa funkcji:       wypelnienie
  parametry wejściowe: A - lista elementów typu logicznego
  wartość zwracana:    brak zwracanej wartości
  informacje:          funkcja wypełnia tablicę A wartościami True
  autor:               961009xxxxx
*********************************************************
"""
def wypelnienie(A: list) -> None:
    for i in range(100):
        A[i] = True


def sito(A: list) -> None:
    n = len(A)
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i] is True:
            for j in range(i, n, i):
                A[j] = False


if __name__ == '__main__':
    A = [None] * 100
    wypelnienie(A)
    sito(A)
    print(f"Liczby pierwsze w przedziale 2..100: ", end='')
    for i in range(2, 100):
        if A[i] is True:
            print(f"{i} ", end='')
