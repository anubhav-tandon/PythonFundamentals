a=input("Enter value of A:")
b=input("Enter value of B:")
c=input("Enter value of C:")
d=b*b-4*a*c
if(d==0):
    print"Equal Roots"
    r=(-b+(d**0.5))/2*a
    print r
elif(d>0):
    print"Different roots"
    r1=(-b+(d**0.5))/2*a
    r2=(-b-(d**0.5))/2*a
    print r1
    print r2
else:
    print"Imaginary Roots"
