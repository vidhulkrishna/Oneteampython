#Fibonacci Sequence

limit=int(input("Enter the limit:"))
f1 = 0
f2 = 1
if limit==1:
    print(f1)
elif limit==2:
    print(f1,f2)
else:
    print("Fibonacci series")
    print(f1)
    print(f2)
    while limit>2:
        f3=f1+f2
        f1=f2
        f2=f3
        print(f3)
        limit-=1    

