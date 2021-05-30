def bubble_sort(itr):
    if len(itr) < 2:
        return itr
    for i in range(len(itr) - 1, 0, -1):
        for j in range(i):
            if itr[j] > itr[j + 1]:
                itr[j + 1], itr[j] = itr[j], itr[j + 1]
    return itr


if __name__ == "__main__":
    lst = [5, 6, 2, 9, 1, 0, 3]
    print(bubble_sort(lst))
