a=int(input("Enter your date:"))
b=int(input("Enter your month:"))
c=int(input("Enter your year:"))
if b in {4,6,9,11}:
    if 1<= a <=30:
        if 0 <= c <=9999:
            print('Your Date',a,'/',b,'/',c,'is valid')
        else:
            print('Your Date',a,'/',b,'/',c,'is invalid')
    else:
       print('Your Date',a,'/',b,'/',c,'is invalid')
if b in {1,3,5,7,8,10,12}:
    if 1<=a<=31:
        if 1<=c<=9999:
            print('Your Date',a,'/',b,'/',c,'is valid')
        else:
            print('Your Date',a,'/',b,'/',c,'is invalid')
    else:
        print('Your Date',a,'/',b,'/',c,'is invalid')
if b==2:
    if 1<=a<=28:
        if 1<=c<=9999 :
            print('Your Date',a,'/',b,'/',c,'is valid')
        if c>9999:
            print('Your Date',a,'/',b,'/',c,'is invalid')
    if a==29:
        if 1<=c<=9999 and c%4==0:
            print("Your Date",a,'/',b,'/',c,'Is valid')
        if c%4!=0:
            print('Your Date',a,'/',b,'/',c,'Is invalid')
    else:
        print('Your Date',a,'/',b,'/',c,'Is invalid')
if b>12:
    print('Your Date',a,'/',b,'/',c,'Is invalid')