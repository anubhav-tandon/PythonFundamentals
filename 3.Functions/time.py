def convert(hr,mins,sec):
    if(sec>=60):
        sec=sec-60
        mins=mins+1
        if(mins>=60):
            mins=mins-60
            hr=hr+1
    print hr,":",mins,":",sec
hr=input("Enter time in hours")
mins=input("Enter time in minutes")
sec=input("Enter time in seconds")
convert(hr,mins,sec)
