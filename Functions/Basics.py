#Without parameters#

#def sum():
#    print("hi")
#print(sum())

#def sum():
 #   a="hi"
  #  return a
#print(sum())
 
#With parameters#

#def sum2(a,b):
 #   c=a+b
  #  return c
#print(sum2(3,2))

#def sum2(n1,n2):
 #   c=n1+n2
  #  return c
#n1=int(input("v1:"))
#n2=int(input("v2:"))
#print(sum2(n1,n2))

#Default parameters#

#def sum2(a=12,b=3):
   # c=a+b
    #return c
#print(sum2())

#def sum2(a=12,b=3):
 #    c=a+b
  #   return c
    
#print(sum2(7))

#Astricts#
def num(*n):
    result=0
    for i in n:
        result =result+i
    return result
print(num(1,2,3,4,5,6))    