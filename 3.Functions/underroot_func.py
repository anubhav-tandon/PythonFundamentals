def roots(a,b,c):
    
    d=b*b-4*a*c
    if(d==0):
        print("Equal roots:")
        r=(-b+(d**0.5))/2*a
        print r
    elif(d>0):
        print("Different roots:")
        r1=(-b+(d**0.5))/2*a
        r2=(-b-(d**0.5))/2*a
        print r1,r2
         
    else:
        print("ImaginaryRoots")

roots(-2,6,1)
