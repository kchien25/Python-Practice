def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while n != 1:
        print(n)
        length += 1
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
        else:
            return "what the heck"
    print(1)
    return length

a = hailstone(27)
print("total sequences is: " + str(a))