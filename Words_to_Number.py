c = input("Enter 'ind' for Indian format and 'west' for western format:")
x = input("Enter Number in words:")
l = x.split(" ")
lf = list(map(lambda x: 1 if x == "one" else x,l))
lf = list(map(lambda x: 2 if x == "two" else x,l))
lf = list(map(lambda x: 3 if x == "three" else x,l))
lf = list(map(lambda x: 4 if x == "four" else x,l))
lf = list(map(lambda x: 5 if x == "five" else x,l))
lf = list(map(lambda x: 6 if x == "six" else x,l))
lf = list(map(lambda x: 7 if x == "seven" else x,l))
lf = list(map(lambda x: 8 if x == "eight" else x,l))
lf = list(map(lambda x: 9 if x == "nine" else x,l))
lf = list(map(lambda x: 10 if x == "ten" else x,l))
for i in range(0,len(lf)):
    if lf[i] == 'hundred':
        print(lf[i-1]*100)
if c == "west":
    print(lf)
elif c == "ind":
    print(lf)
