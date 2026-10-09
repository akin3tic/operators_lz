c = 0
n = int(input("vvedyte chislo n "))
if n>=1 and n<=25: 
    for i in range(2,n-1):
        if n/i == 0:
            c +=1
    if c>0:
        print("N")
    else:
        print("Y")
else:
    print("введенное n не попадает в интервал [1,25]")