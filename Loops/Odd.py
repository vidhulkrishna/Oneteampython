s_limit=int(input())
e_limit=int(input())
print("Odd numbers are:")
while s_limit<=e_limit:
    if s_limit %2 !=0:
        print(s_limit)
        s_limit+=1  