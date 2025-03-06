n=int(input("Enter Number"))
sum=0
while n>0:
    dig=n%10
    sum+=dig
    n=n//10
print(sum)
