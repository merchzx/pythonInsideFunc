from typing import Union, List


# def min_max(lst: list[int, float]) -> tuple:
#     def maxx():
#         return max(lst)
#
#     def minn():
#         return min(lst)
#
#     return maxx, minn
#
#
# res = (min_max([4, 5, 6, 7, 8, 1.2]))
# print(res[0]())
# print(res[1]())


def square_of_number(lst: list[Union[int, float]]) -> list[Union[int, float]]:
    lst2 = []

    def go_to_square(i: Union[int, float]):
        lst2.append(i)

    for i in lst:
        if i % 2 == 0:
            go_to_square(i * i)
    return lst2


res = square_of_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 16, 18])
print(res)
