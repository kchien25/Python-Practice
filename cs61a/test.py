def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True
    
def t():
    return print(print(1))

def f():
    return -1

with_if_statement()
