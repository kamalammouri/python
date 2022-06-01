def classer(list_dec):
    vide=0
    for x in range(len(list_dec)):
        for y in range(len(list_dec)):
            if list_dec[y]["note"] < list_dec[x]["note"]:
                vide=list_dec[x]
                list_dec[x]=list_dec[y]
                list_dec[y]=vide
    return list_dec
    

eleve= [{'nom':'Karim','note':13.4}, {'nom':'Ahmed', 'note':12}, {'nom':'Salim', 'note':10},
{'nom':'Meriem', 'note':15}, {'nom':'Hanan', 'note':9.5}]

for i in classer(eleve):
    print(i)