x = [10,20,30,40]

#Aliasing is process to give another name to a list
y = x
#now list x have another name or alias y

print(y)
print()
y[1] = 100
print(x)

print()

#Cloning is used to copy a list using slicing operator
a = [1,2,3,4,5]
b = a[:]

print(b)
#in cloning a and b are 2 independent lists