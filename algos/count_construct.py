# brute force
def count_construct(target_text, word_bank):
    if target_text == "": return True
    total_count = 0
    for word in word_bank:
        if target_text.startswith(word):
            no_of_ways = count_construct(target_text[len(word):], word_bank)
            total_count += no_of_ways
    return total_count


# memoization
def count_construct_m(target_text, word_bank, memo={}):
    if target_text in memo: return memo[target_text]
    if target_text == "": return True
    total_count = 0
    for word in word_bank:
        if target_text.startswith(word):
            no_of_ways = count_construct_m(target_text[len(word):], word_bank, memo)
            total_count += no_of_ways
    memo[target_text] = total_count
    return total_count


# tabulation
def count_construct_t(target_text, word_bank):
    table = [0] * (len(target_text) + 1)
    table[0] = 1

    for i in range(len(target_text)):
        if table[i]>0:
            for word in word_bank:
                if target_text[i:].startswith(word):
                    table[i + len(word)] += table[i]
    return table[-1]


if __name__ == "__main__":
    print(count_construct("aaaaaaaaaaaae", ["aaa", "aaaaaa", "e", "a"]))
    print(count_construct_m("aaaaaaaaaaaae", ["aaa", "aaaaaa", "e", "a"]))
    print(count_construct_t("aaaaaaaaaaaae", ["aaa", "aaaaaa", "e", "a"]))
