f=open("test.txt",'r')
line1=f.readline()
line2=f.readline()
line3=f.readlines()
f.close()

print(line1,end="")
print(line2,end="")
print(line3)
