# brute force
def can_construct(target_text, word_bank):
    if target_text == "": return True

    for word in word_bank:
        if target_text.startswith(word):
            return can_construct(target_text[len(word):], word_bank)
    return False


# memoization
def can_construct_m(target_text, word_bank, memo={}):
    if target_text in memo: return memo[target_text]
    if target_text == "": return True

    for word in word_bank:
        if target_text.startswith(word):
            memo[target_text] = can_construct_m(target_text[len(word):], word_bank)
            return memo[target_text]
    return False


# tabulation
def can_construct_t(target_text, word_bank):
    table = [False] * (len(target_text) + 1)
    table[0] = True

    for i in range(len(target_text)):
        if table[i]:
            for word in word_bank:
                if target_text[i:].startswith(word):
                    table[i + len(word)] = True
    return table[len(target_text)]


if __name__ == "__main__":
    print(can_construct("aaaaaaaaaaaae", ["aaaa", "a", "aaaaaaa"]))
