def palind(a):
    rev = ''
    for i in a:
        rev = i + rev  
    if a == rev:
        print("palimdrome")
    else:
        print(" not ")
print(palind("amma"))