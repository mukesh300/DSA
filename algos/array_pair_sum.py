# Array Pair Sum
# Given an integer array, output all the unique pairs that sum up to a specific value k.

def pair_sum(target, arr):
    if len(arr) < 2: return []

    seen = set()
    output = set()
    for n in arr:
        k = target - n

        if k not in seen:
            seen.add(n)
        else:
            output.add((k, n))

    return output


if __name__ == "__main__":
    print(pair_sum(4, [2, 3, 1, 2, 4]))
