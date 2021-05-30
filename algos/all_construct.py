import timeit

def timer(function):
  def new_function(*args, **kwargs):
    start_time = timeit.default_timer()
    function(*args, **kwargs)
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()

# brute force
@timer
def all_construct(target_text, word_bank):
    if target_text == "": return [[]]
    result = []
    for word in word_bank:
        if target_text.startswith(word):
            suffix_ways = all_construct(target_text[len(word):], word_bank)
            target_ways = list(map(lambda x: [word] + x, suffix_ways))
            result.extend(target_ways)
    return result


# memoization
@timer
def all_construct_m(target_text, word_bank, memo={}):
    if target_text in memo: return memo[target_text]
    if target_text == "": return [[]]
    result = []
    for word in word_bank:
        if target_text.startswith(word):
            suffix_ways = all_construct_m(target_text[len(word):], word_bank, memo)
            target_ways = list(map(lambda x: [word] + x, suffix_ways))
            result.extend(target_ways)
    memo[target_text] = result
    return result


# tabulation
@timer
def all_construct_t(target_text, word_bank):
    table = [None] * (len(target_text) + 1)
    table[0] = [[]]
    for i in range(len(target_text)):
        if table[i] is not None:
            for word in word_bank:
                if target_text[i:].startswith(word):
                    sufix_ways = list(map(lambda x: x + [word], table[i]))
                    if table[i + len(word)] is None:
                        table[i + len(word)] = sufix_ways
                    else:
                        table[i + len(word)].extend(sufix_ways)
    return table[-1]


if __name__ == "__main__":
    print(all_construct("aaaaabaaaaaae", ["aaa", "aabaaa", "e", "a"]))
    print(all_construct_m("aaaaabaaaaaae", ["aaa", "aabaaa", "e", "a"]))
    print(all_construct_t("aaaaabaaaaaae", ["aaa", "aabaaa", "e", "a"]))
