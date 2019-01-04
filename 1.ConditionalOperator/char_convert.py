x=raw_input("Enter any character:")
if(x>='a' and x<='z'):
    x=chr(ord(x)-32)
else:
    x=chr(ord(x)+32)

print x
