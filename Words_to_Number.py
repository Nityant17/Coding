c = input("Enter 'ind' for Indian format and 'west' for western format:")
x = input("Enter Number in words:")
l = x.split(" ")
lf = list(map(lambda x: 1 if x == "one" else x,l))
for i in range(0,len(lf)):
    if lf[i] == 'hundred':
        print(lf[i-1]*100)
if c == "west":
    print(lf)
elif c == "ind":
    print(lf)
