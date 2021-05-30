# anagram
def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    dict_chars = {}

    for s in s1:
        if s in dict_chars:
            dict_chars[s] += 1
        else:
            dict_chars[s] = 1

    for s in s2:
        if s in dict_chars:
            dict_chars[s] -= 1
        else:
            return False
    for k, v in dict_chars.items():
        if v != 0:
            return False
    return True


if __name__ == "__main__":
    print(anagram("Astronomer", "Moon starer"))
