def divice(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Aie, code contient une division par zero")
    except TypeError:
        print("Aie, Vous saisire un caracter")
    else: 
        print(f"la,resultat est {result}")
    finally:
        print("toujour execute")
    
divice(1,2)
divice(1,0)
divice('1','2')