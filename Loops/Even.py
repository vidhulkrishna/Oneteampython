s_limit=int(input())
e_limit=int(input())
print("Even numbers are:")
while s_limit<=e_limit:
    if s_limit %2 !=0:
        print(s_limit)
    s_limit+=1  