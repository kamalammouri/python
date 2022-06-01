import string

def compter_mots(phr):
    alpha_lower = string.ascii_lowercase
    for x in phr:
        if(x.lower() not in alpha_lower and x!=" "):
            char=x
    
    phr=phr.replace(char,'')
    phr=phr.split()
    
    word={}
    
    for x in range(len(phr)):
        phr[x]=phr[x].lower()
        count = phr.count(phr[x])
        word[phr[x]]=count
    return word


phrase="What a nice day? what a loveley day"
    
print(compter_mots(phrase))
