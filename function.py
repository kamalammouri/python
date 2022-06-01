def yes_or_no(prompt,retries=3,reminder='Esseyer encore'):
    """yes_or_no?!"""
    
    while True:
        ok=prompt
        if ok in ('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries-=1
        
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)
        

yes_or_no("okay")
yes_or_no("okay",2)
yes_or_no("okay",2,"error")
