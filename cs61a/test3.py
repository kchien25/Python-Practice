def keep_ints(n):
    def cond(is_even):
        x = 1
        while x < n:
            if is_even(x):
                print(x)
            x += 1
    return cond

def is_even(x):
    return x % 2 == 0

keep_ints(5)(is_even)