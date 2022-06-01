import string
alpha = string.ascii_lowercase
z=0

for x in range(len(alpha)):
    for y in range(len(alpha)):
        if alpha[x]!=alpha[y]:
            print(alpha[x],alpha[y])
            
for x in alpha:
    for y in alpha:
        if x!=y:
            print(x+y)
            z+=1

print(z)