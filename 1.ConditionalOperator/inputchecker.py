print"Enter input inside ' '"
x=input("Enter value of x:")
if(x>='A' and x<='Z'):
    print"Upper case"
elif(x>='a' and x<='z'):
    print"Lower case"
elif(x>=0 and x<=9):
    print"Digit"
else:
    print"Invalid Input!!"
