b,q,n = map(int, input("vvedyte znacheniye первого элемента прогрессии b, множитель прогрессии q и номер последнего элемента n. ").split())
if b>=-10000 and b<=10000 and q>=1 and q<=50 and n>=2 and n<=100:
    print("summa geomitricheskoi progresii: ", (b*(1-q**n))/(1-q))