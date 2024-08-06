a = [1, 4, 5, 6, 3, 7]
odd = []
even = []

for i in range(len(a)):
    if a[i] % 2 == 0:  # Check if the value at index i is even
        even.append(a[i])
    else:
        odd.append(a[i])

print("Even numbers:", even)
print("Odd numbers:", odd)
