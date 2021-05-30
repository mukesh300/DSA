def merge(left, right, lst):
    n_left, n_right = len(left), len(right)
    i, j, k = 0, 0, 0

    while n_left > i and n_right > j:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < n_left:
        lst[k] = left[i]
        i += 1
        k += 1
    while j < n_right:
        lst[k] = right[j]
        j += 1
        k += 1


def merge_sort(lst):
    if len(lst) < 2:
        return
    mid_index = len(lst) // 2
    left = lst[0:mid_index]
    right = lst[mid_index:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, lst)


if __name__ == "__main__":
    lst = [5, 6, 2, 9, 1, 0, 3]
    merge_sort(lst)
    print(lst)
