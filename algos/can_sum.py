# write a function can_sum that takes in a target_sum and a list of numbers as arguments
# The function should return a bolean indicating whether or not it is possible to generate the target_sum using numbers from list.
# you may use an element of the list as many times as needed.
# You may assume that all input numbers are non-negative.

# brute force
def can_sum(target_sum, arr):
    if target_sum < 0: return False
    if target_sum == 0: return True

    for element in arr:
        if can_sum(target_sum - element, arr):
            return True
    return False


# memoization
def can_sum_m(target_sum, arr, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum < 0: return False
    if target_sum == 0: return True

    for element in arr:
        memo[target_sum] = can_sum(target_sum - element, arr)
        if memo[target_sum]:
            return True
    return False


# tabulation
def can_sum_t(target_sum, arr):
    table = [False] * (target_sum + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in arr:
                if i + num <= target_sum:
                    table[i + num] = table[i]

    return table[target_sum]


if __name__ == "__main__":
    print(can_sum_t(5, [4, 3, 0, 8]))
