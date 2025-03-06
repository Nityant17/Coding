def fib(n):
    # Stop condition
    if (n==0):
        return 0
    # Stop condition
    if (n==1 or n==2):
        return 1
    # Recursion function
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("Enter Number of Terms:"))
print("Fibonacci series of",n,"numbers is :",end=" ")
for i in range(0,n): 
    print(fib(i),end=" ")
