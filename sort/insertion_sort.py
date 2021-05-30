def insertion_sort(lst):
    if len(lst) < 2:
        return lst
    for i in range(1, len(lst)):
        anchor = lst[i]
        j = i - 1
        while j >= 0 and anchor < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = anchor
    return lst


if __name__ == "__main__":
    lst = [5, 6, 10, 2, 9, 1, 0, 3]
    print(insertion_sort(lst))

