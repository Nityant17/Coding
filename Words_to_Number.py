c = input("Enter 'ind' for Indian format and 'west' for western format:")
a = input("Enter Number in words:")
x = a.lower()
l = x.split(" ")
lf = l.copy()
for i in range(0,len(lf)):
    if lf[i] == "zero":
        lf[i] = 0
        l[i] = 0
    elif lf[i] == "one":
        lf[i] = 1
        l[i] = 1
    elif lf[i] == "two":
        lf[i] = 2
        l[i] = 2
    elif lf[i] == "three":
        lf[i] = 3
        l[i] = 3
    elif lf[i] == "four":
        lf[i] = 4
        l[i] = 4
    elif lf[i] == "five":
        lf[i] = 5
        l[i] = 5
    elif lf[i] == "six":
        lf[i] = 6
        l[i] = 6
    elif lf[i] == "seven":
        lf[i] = 7
        l[i] = 7
    elif lf[i] == "eight":
        lf[i] = 8
        l[i] = 8
    elif lf[i] == "nine":
        lf[i] = 9
        l[i] = 9
    elif lf[i] == "ten":
        lf[i] = 10
        l[i] = 10
    elif lf[i] == "eleven":
        lf[i] = 11
        l[i] = 11
    elif lf[i] == "twelve":
        lf[i] = 12
        l[i] = 12
    elif lf[i] == "thirteen":
        lf[i] = 13
        l[i] = 13
    elif lf[i] == "fourteen":
        lf[i] = 14
        l[i] = 14
    elif lf[i] == "fifteen":
        lf[i] = 15
        l[i] = 15
    elif lf[i] == "sixteen":
        lf[i] = 16
        l[i] = 16
    elif lf[i] == "seventeen":
        lf[i] = 17
        l[i] = 17
    elif lf[i] == "eighteen":
        lf[i] = 18
        l[i] = 18
    elif lf[i] == "nineteen":
        lf[i] = 19
        l[i] = 19
    elif lf[i] == "twenty":
        lf[i] = 20
        l[i] = 20
    elif lf[i] == "thirty":
        lf[i] = 30
        l[i] = 30
    elif lf[i] == "forty":
        lf[i] = 40
        l[i] = 40
    elif lf[i] == "fifty":
        lf[i] = 50
        l[i] = 50
    elif lf[i] == "sixty":
        lf[i] = 60
        l[i] = 60
    elif lf[i] == "seventy":
        lf[i] = 70
        l[i] = 70
    elif lf[i] == "eighty":
        lf[i] = 80
        l[i] = 80
    elif lf[i] == "ninety":
        lf[i] = 90
        l[i] = 90
    elif lf[i] == "hundred":
        lf[i] = 100
    elif lf[i] == "thousand":
        lf[i] = 1000
    elif lf[i] == "million":
        lf[i] = 1000000
    elif lf[i] == "billion":
        lf[i] = 1000000000
    elif lf[i] == "trillion":
        lf[i] = 1000000000000
    elif lf[i] == "lakhs" or lf[i] == "lakh":
        lf[i] = 100000
    elif lf[i] == "crore":
        lf[i] = 10000000
print(l)
print(lf)
for i in range(0,len(lf)):
    if lf[i] == 1000000:
        lt = lf[i-1]*1000000
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
