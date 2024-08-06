lw_limit=int(input("first limit:"))
upr_limit=int(input("last limit:"))
for i in range(lw_limit,upr_limit+1):
    s=0
    temp=i
    for j in range(1,i+1):
        d=i%10
        s=s+d**3
        i//=10
    if temp==s:
        print(temp)
        