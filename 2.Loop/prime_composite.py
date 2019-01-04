i=input("Enter total numbers:")
c=0
p=0
while(i!=0
      ):
    n=input("Enter the number")
    for j in range(2,n):
        if(n%j==0):
            c=c+1
            break
        else:
            p=p+1
            break
    i=i-1
print"Number of Prime Number:",p
print"Number of Composite Number:",c
