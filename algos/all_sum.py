## return all combinations of numbers in a list which sum up to the given number

## recursion
def all_sum(m, lst):
    result = []
    if m==0: return [[]]
    if m<0: return 

    for i in lst:
        res = all_sum(m-i, lst)
        if res is not None:
            for r in res:
                result.append([i] + r)
    return result

all_sum(15, [10, 5, 15])
