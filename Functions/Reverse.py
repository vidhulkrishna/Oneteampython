def revs(n):
    rev=0
    while n!=0:
        d=n%10
        rev=(rev*10)+d
        n//=10  
    return rev
print(revs(987))
