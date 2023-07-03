import random
import sys


def bubblesort(elements: list) -> None:
    num_elems = len(elements)
    for i in range(num_elems):
        for j in range(i, num_elems):
            if elements[i] > elements[j]:
                elements[i], elements[j] = elements[j], elements[i]


if __name__ == '__main__':
    elements_to_sort = []
    for _ in range(100):
        elements_to_sort.append(random.randint(0, 1000))
    print(f"Przed sortowaniem: {', '.join([str(x) for x in elements_to_sort])}")

    bubblesort(elements_to_sort)

    print(f"Po sortowaniu: {', '.join([str(x) for x in elements_to_sort])}")
