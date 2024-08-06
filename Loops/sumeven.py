#Write a Python program to   takes two integers, start and end, and returns the sum of all even numbers

n1=int(input("Enter the start num:"))
n2=int(input("Enter the end num:"))
sum=0
while n1<=n2:
    if n1%2==0:
        sum=sum+n1
    n1+=1
print("Sum is :",sum)    


    
