#sumd==productd
n=int(input("Value:"))
sum=0
prd=1
while n!=0:
    d=n%10
    sum=sum+d
    prd=prd*d
    n//=10