# func fib(n) takes a no. as argument and returns nth no. of fibonacci seq

# recursion
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


# memoization
def fib_m(n, memo={}):
    if n in memo: return memo[n]
    if n in [1, 2]: return 1
    memo[n] = fib_m(n - 1, memo) + fib_m(n - 2, memo)
    return memo[n]


# tabulation
def fib_t(n):
    table = [0] * (n)
    table[0], table[1] = 1, 1
    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]
    return table[n - 1]


if __name__ == "__main__":
    print(fib(5), fib_m(50), fib_t(50))
