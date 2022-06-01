
def fahrenteit_to_celsius(deg):
    Cel = (deg - 32) * 5/9
    return Cel

def celsius_to_fahrenteit(deg):
    Fah = (deg * 9/5) + 32
    return Fah

assert celsius_to_fahrenteit(100) == 212,"error 1"
assert fahrenteit_to_celsius(32) == 0,"error 2"
