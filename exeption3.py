def divParZero():
    x=11/0
    
try:
    divParZero()
except ZeroDivisionError as e:
    print("Aie, code contient une division par zero")
else: 
    print("ton code n'a pas leve d'exceptions")
finally:
    print("toujour execute")