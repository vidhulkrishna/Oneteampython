
limit = int(input("Enter the limit "))
prime = []
not_prime = []
for i in range(limit):
    e = int(input("Element "))
    for j in range(2,e):
        if e%j==0:
            not_prime.append(e)
            break
    else:
        prime.append(e)
print(prime)
print(not_prime)