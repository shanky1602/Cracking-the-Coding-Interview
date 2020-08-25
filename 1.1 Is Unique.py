s=input()
d=set()
for i in s:
    if i in d:
        print("not unique")
        break
    else:
        d.add(i)
else:
    print("unique")
