n = int(input("Enter n:"))
ctr=1
for i in range (0,(2*n-1)):
    l=[n]*(2*n-1)
    mi=(2*n-2)//2
    if (i<=mi):
        l[mi]=n-i
    else:
        ctr+=1
        l[mi]=ctr
    me=l[mi]
    terms=((2*me-2)//2)
    for k in range(1,terms+1):
        l[mi-k]=me
        l[mi+k]=me
    for v in range(1,mi+1):
        if (mi-terms-v > 0):
            l[mi-terms-v]=me+v
            l[mi+terms+v]=me+v
    print(l)
