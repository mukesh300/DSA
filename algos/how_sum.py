# brute force
def how_sum(target_sum, arr):
    if target_sum < 0: return None
    if target_sum == 0: return []

    for element in arr:
        remainder_result = how_sum(target_sum - element, arr)
        if remainder_result is not None:
            return remainder_result + [element]
    return None


# memoization
def how_sum_m(target_sum, arr, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum < 0: return None
    if target_sum == 0: return []

    for element in arr:
        remainder_result = how_sum(target_sum - element, arr)
        if remainder_result is not None:
            memo[target_sum] = remainder_result + [element]
            return memo[target_sum]
    return None


# tabulation
def how_sum_t(target_sum, arr):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for elements in arr:
                if i + elements <= target_sum:
                    table[i + elements] = table[i] + [elements]
            if table[target_sum] is not None: return table[target_sum]

    return table[target_sum]


if __name__ == "__main__":
    print(how_sum_t(5, [3, 7, 6, 9, 13, 2, 12]))
