def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

"""
Despite the doctests above, this function actually does not do the same thing as an 
if statement in all cases. To prove this fact, write functions c, t, and f such that 
with_if_statement returns the number 1, but with_if_function does not (it can do 
anything else):
"""

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return print("1")

def t():
    return print(True)

def f():
    return False

with_if_function()

