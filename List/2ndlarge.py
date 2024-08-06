a=[23,5,67,38,25]
lg=0
for i in range(len(a)):
    if a[i]>lg:
        lg=a[i]
print(lg)
i=0
while(1):
    if a[i]!=lg:
        sbig=a[i]
        break
    i+=1
for i in range(i+1,len(a)):
        if a[i]<lg and a[i]>sbig:
            sbig=a[i]
print("big:",lg)
print("sbig:",sbig)        


