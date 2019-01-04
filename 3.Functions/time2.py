name=''
def convert(hr,mins,sec):
    if(sec>=60):
        sec=sec-60
        mins=mins+1
        if(mins>=60):
            mins=mins-60
            hr=hr+1
    print hr,":",mins,":",sec

if _name_=='_main_':
    main()
