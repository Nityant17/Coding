a = ["a", "b", "c"]

for i, name in enumerate(a):
    print(f"Index {i}: {name}")

print(list(enumerate(a)))

for index, x in enumerate(a, start=1):
    print(index, x)

for ele in enumerate(a):
    print (ele)

