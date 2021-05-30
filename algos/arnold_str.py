def arnold_str(arr):
    for num in arr:
        lst = map(int, list(str(num)))
        total = 0
        for n in lst:
            total += (n ** 3)
        if total == num:
            print(f"{num} is an arnold str")
        else:
            print(f"{num} is not an arnold str")


arnold_str([153, 234])
