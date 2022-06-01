f=open("test.txt","w")
for x in range(20):
    f.write(f'start msedge --profile-directory="person {x}" -incognito "http://www.google.com"\n')
f.close()
