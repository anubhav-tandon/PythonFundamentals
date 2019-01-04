def count(x):
    u=0
    l=0
    d=0
    inv=0
    for i in range(0,len(x)):
        if(x[i]>='A' and x[i]<='Z'):
            u=u+1        
        elif(x[i]>='a' and x[i]<='z'):
            l=l+1
        elif(x[i]>='0' and x[i]<='9'):
            d=d+1
        else:
            inv=inv+1
    print "Upper case:",u,"Lower case",l,"Digit",d,"Invalid inputs:",inv

x=input("Enter string inside ' ' : ")
count(x)
