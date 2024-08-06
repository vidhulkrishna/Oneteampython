def fact(n):
    if n==0:
        return "no result"
    elif n==1:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result*=i
        return result
print(fact(5))                