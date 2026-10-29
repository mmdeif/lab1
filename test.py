from algorithms import pointers
from algorithms import bin_s
from algorithms import point_2
from algorithms import binar2
def test(f):
    tests = [
        ([1, 2, 3], [3, 4, 5], True),
        ([2, 4, 6], [3, 5, 7], False),
        ([1, 2], [], False),
        ([7], [3], False),
        ([1, 5, 9], [0, 5, 10], True),
        ([2, 2, 2], [3, 3, 3], False),
        ([1, 1, 4], [4, 4, 8], True),
        ([0, 998], list(range(0, 1000, 2)), True),
        ([1, 999], list(range(0, 1000, 2)), False),
        ([3, 301, 778], list(range(0, 1000, 2)), True),
        ([], [], False),
        ([], [4, 5], False),
        ([5], [5], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([-4, 0, 6], [-5, 0, 2], True),
        ([1, 3, 5, 7, 9], [0, 2, 4, 6, 8], False),
    ]

    for a, b, expected in tests:
        result = f(a, b)

        assert result == expected, (
            f"Ошибка: a={a}, b={b}, "
            f"ожидалось {expected}, получено {result}"
        )

    print("Все тесты пройдены!")

test(pointers)
test(bin_s)
test(point_2)
test (binar2)