#Write a Python program to  takes an 
# integer n and returns True if the 
# number is prime, and False otherwise.

n=int(input("Enter the num:"))
i=2
while i<n:
    if n%i==0:
        print("False")
        break
    i+=1
else:
    print("True")