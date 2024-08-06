#Write a Python program to   takes an 
# integer n and prints the numbers from 
# 1 to n. For multiples of three, 
# print "Fizz" instead of the number and 
# for the multiples of five,
#  print "Buzz". For numbers which 
# are multiples of both three and five, 
# print "FizzBuzz".

n=int(input("Enter a number:"))
i=1
while i<=n:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
    i+=1    
