def factorial(n):
    if n <= 1:
        return 1
    else:
        fact=n*factorial(n-1)
    return fact
x=int(input("Enter No. :")) 
print(factorial(x))
