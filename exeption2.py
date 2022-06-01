while True:
    try:
        x=int(input("please entre un number:"))
        print(f"Merci davoir sasire valide {x}")
        break
    except ValueError as e:
        print("desole! vous saisire un entier")
        print(e)