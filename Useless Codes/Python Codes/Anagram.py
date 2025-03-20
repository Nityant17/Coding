x=input("Enter Str1 :")
y=input("Enter Str2 :")
a=x.lower().replace(" ","")
b=y.lower().replace(" ","")
p=list(a)
q=list(b)
if (p.sort()==q.sort()):
    print("ANAGRAM")
else:
    print("NOT ANAGRAM")
