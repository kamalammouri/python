import ops

a=int(input('Entre a \t'))
b=int(input('Entre b \t'))
op=input("+ , - , / , // , * \n")

if op=="+":
    print(ops.add(a,b))
elif op=="-":
    print(ops.sub(a,b))
elif op=="/":
    print(ops.div(a,b))
elif op=="*":
    print(ops.mult(a,b))
elif op=="//":
    print(ops.div_entier(a,b))
else: print('bad ope')