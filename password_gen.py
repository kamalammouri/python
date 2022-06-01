import  random as rand
import string

def pass_gen(lenght,with_digits,with_uppercase):
    
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    digits = string.digits
    
    if with_uppercase & with_digits:
        all = alpha_upper + alpha_lower + digits
        if(lenght==3):
            
            return rand.sample([alpha_upper,alpha_lower,digits],counts=[1,1,1],k=3)
    elif with_digits:
        all = digits + alpha_lower
    elif with_uppercase:
        all = alpha_upper + alpha_lower
    else:
        all = alpha_lower 
    
    password = rand.sample(all,lenght)
    password = "".join(password)
    return password
    
    


print(pass_gen(3,True,True))
print(pass_gen(3,True,True))
print(pass_gen(3,True,True))
