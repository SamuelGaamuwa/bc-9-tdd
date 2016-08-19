def super_sum(*args):
    total = 0
    for value in args:
        if isinstance(value, list):
            super_sum(value)
        elif isinstance(value, str):
        	continue
        else:
            total = total + value
    return total

print (super_sum(2, 3.5))