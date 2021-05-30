def partition(itr, start, end):
    pivot = end
    pindex = start
    for i in range(start, end):
        if itr[i] <= itr[pivot]:
            itr[pindex], itr[i] = itr[i], itr[pindex]
            pindex += 1
    itr[pindex], itr[pivot] = itr[pivot], itr[pindex]
    return pindex


def quick_sort(itr, start, end):
    if start >= end:
        return
    pindex = partition(itr, start, end)
    quick_sort(itr, start, pindex - 1)
    quick_sort(itr, pindex + 1, end)
    return itr


if __name__ == "__main__":
    lst = [5, 6, 2, 9, 1, 0, 3]
    print(quick_sort(lst, 0, len(lst) - 1))
