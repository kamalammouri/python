def select_student_ok(list,seuil):
    ok={"Accepted":0,"Refused":0}
    accp=[]
    reff=[]
    for x in list:
        if(x[1]<=seuil):
            reff.append(x)
        else:
            accp.append(x)
    reff.sort(key=lambda k: k[1])
    accp.sort(key=lambda k: k[1],reverse=True)
    ok["Accepted"]=accp
    ok["Refused"]=reff
    return ok

select_student_ok([["Kermit Wade", 27],["Hattie Schleusner", 67],["Ben Ball", 5],["William Lee", 2]],20)

