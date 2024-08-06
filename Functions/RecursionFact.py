def recursion_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursion_fact(n - 1)

s = recursion_fact(5)
print(s)
