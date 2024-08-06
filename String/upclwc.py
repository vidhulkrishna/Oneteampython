a=str(input("Enter ur string:"))
r=''
for i in range(len(a)):
    if i%2==0:
      r+=a[i].upper()
      
      print()