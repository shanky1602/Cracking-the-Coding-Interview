s=input()
d={}
c=0
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
if len(s)%2==0:
    for i in d:
        if d[i]%2==0:
            pass
        else:
            print("false")
            break
    else:
        print("true")
else:
    for i in d:
        if d[i]%2!=0:
            c+=1
    if c==1:
        print("true")
    else:
        print("false")
