from ops import add,div,mult,sub,div_entier

a=int(input('Entre a \t'))
b=int(input('Entre b \t'))
op=input("+ , - , / , // , * \n")

if op=="+":
    print(add(a,b))
elif op=="-":
    print(sub(a,b))
elif op=="/":
    print(div(a,b))
elif op=="*":
    print(mult(a,b))
elif op=="//":
    print(div_entier(a,b))
else: print('bad ops')