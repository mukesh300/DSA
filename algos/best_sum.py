# brute force
def best_sum(target_sum, arr):
    if target_sum == 0: return []
    if target_sum < 0: return

    shortest_combination = None
    for element in arr:
        remainder_result = best_sum(target_sum - element, arr)
        if remainder_result is not None:
            combination = remainder_result + [element]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination

    return shortest_combination

# memoization
def best_sum_m(target_sum, arr, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return

    shortest_combination = None
    for element in arr:
        remainder_result = best_sum_m(target_sum - element, arr, memo)
        if remainder_result is not None:
            combination = remainder_result + [element]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return memo[target_sum]

# tabulation
def best_sum_t(target_sum, arr):
    table = [None]*(target_sum+1)
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for element in arr:
                if i+element <= target_sum:
                    table[i+element] = table[i]+[element] if table[i+element] is None else (table[i]+[element] if len(table[i]+[element]) < len(table[i+element]) else table[i+element])

    return table[target_sum]

if __name__ == "__main__":
    print(best_sum_t(6, [1, 3, 7, 6, 9, 13, 2, 12]))
