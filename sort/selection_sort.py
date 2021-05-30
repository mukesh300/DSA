def selection_sort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    lst = [5, 6, 10, 2, 9, 1, 0, 3, 8, 90]
    selection_sort(lst)
    print(lst)
