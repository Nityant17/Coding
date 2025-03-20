d=eval(input("Enter List of Dictionaries:"))
k=input("Enter key:")
print(sorted(d, key=lambda x: x[k]))
