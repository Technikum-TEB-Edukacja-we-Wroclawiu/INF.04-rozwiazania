# INF.04-01-25.06-SG
import random
from collections import Counter


def draw(num_draws: int, draws: list[list[int]]):
    for i in range(num_draws):
        single_draw = random.sample(population=range(1, 50), k=6)
        draws.append(single_draw)


def show_results(draws: list[list[int]]):
    """
    ************************
    nazwa funkcji: show_results
    opis funkcji: funkcja wyświetla rezultaty wszystkich losowań - wylosowane liczby
    parametry: draws - lista wyników losowań, wynik losowania jest listą
    zwracany typ i opis: brak
    autor: 8-22403
    ************************
    """
    for i in range(len(draws)):
        print(f"Losowanie {i + 1}: {' '.join(str(x) for x in draws[i])}")


def show_elements_count(draws: list[list[int]]):
    counter = Counter()
    for draw in draws:
        counter.update(draw)

    for i in range(1, 50):
        print(f"Wystąpienia liczby {i}: {counter[i]}")


def main():
    num_draws = int(input("Ile wygenerować losowań? "))

    draws = []
    draw(num_draws, draws)

    show_results(draws)

    show_elements_count(draws)


if __name__ == '__main__':
    main()
