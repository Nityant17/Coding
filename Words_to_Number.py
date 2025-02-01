c = input("Enter 'ind' for Indian format and 'west' for western format:")
a = input("Enter Number in words:")
x = a.lower()
l = x.split(" ")
lf = l.copy()

word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, 
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, 
    "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000, 
    "trillion": 1000000000000, "lakh": 100000, "lakhs": 100000, "crore": 10000000
}

for i in range(len(lf)):
    if lf[i] in word_to_num:
        lf[i] = word_to_num[lf[i]]
        if lf[i] <= 90: 
            l[i] = lf[i]

i = 0
while i < len(lf)-1:
    if len(lf) == 2:
        if any(isinstance(b,str) for b in l):
            lt = lf[0]*lf[1]
            break
        else:
            lt = lf[0]+lf[1]
            break
    else:
        if (i+1) < len(l):
            if isinstance(l[i], int) and isinstance(l[i + 1], int):
                l[i] += l[i+1]
                lf[i] += lf[i + 1]
                del l[i+1]
                del lf[i + 1]
            else: i+=1    

i=0
while i < len(l):
    if i+1<len(l) and l[i] == 'hundred':
        l[i-1]*=100
        lf[i-1]*=100
        del l[i]
        del lf[i]
        if isinstance(l[i-1], int) and isinstance(l[i], int):
                l[i-1] += l[i]
                lf[i-1] += lf[i]
                del l[i]
                del lf[i]
    i+=1

if len(lf) == 1: lt = lf[0]
if len(lf) == 2:
    if any(isinstance(b,str) for b in l):
        lt = lf[0]*lf[1]
    else:
        lt = lf[0]+lf[1]
if len(lf) > 2:
    ts = 0
    o = 0
    while o < len(l):
        ifl=l[o]
        o+=1
        pd = 1*ifl
        while o < len(l) and isinstance(l[o],str):
            pd*=lf[o]
            o+=1
        ts+=pd
    lt=ts

ln = [d for d in str(lt)]
cn = 1
li = []
if c == "west":
    for i in range(len(ln)-1,-1,-1):
        if cn%3 == 0:
            li.append(i)
            cn+=1
        else:
            cn+=1
elif c == "ind":
    for i in range(len(ln)-1,-1,-1):
        if cn == 3:
            li.append(i)
            cn = 5
        elif (cn%2 == 0 and cn>3):
            li.append(i)
            cn+=1
        else:
            cn+=1

li.sort()
cnt=0
for i in range(0,len(li)):
    if li[i] != 0:
        li[i]+=cnt
        cnt+=1
for i in li:
    if i != 0:
        ln.insert(i,",")
for i in ln:
    print(i,end="")
    
