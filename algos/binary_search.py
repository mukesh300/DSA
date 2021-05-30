def binary_search(itr, value):
    if len(itr) == 0:
        return []
    left_index, right_index = 0, len(itr) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if itr[mid_index] == value:
            return True
        elif itr[mid_index] < value:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return False


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(lst, 30))
