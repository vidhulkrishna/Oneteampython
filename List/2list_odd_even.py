o=[1,4,5,6,3,7]
e=[55,67,8,23,80]
o.extend(e)
e.clear()
for i in e:
    if i%2==0:
      o.append(i)
    else:
      o.append(i)
      e.remove(i)
print(o)
print(e)


