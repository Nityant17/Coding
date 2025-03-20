def flatten(l):
    ln=[]
    for i in l:
        if type(i)==list:
            ln.extend(flatten(i))
        else:
            ln.append(i)
    return ln
l=eval(input("Enter list :")) 
print(flatten(l))
