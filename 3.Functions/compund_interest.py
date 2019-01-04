p=input("Enter principal:")
t=input("Enter time in years  :")
r=input("Enter rate:")
n=input("Enter intrest compounded per year:")

x=lambda n,r:1+r/n
amt=p*(x(n,r)**(n*t))
print amt
