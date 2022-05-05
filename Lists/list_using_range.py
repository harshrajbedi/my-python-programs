# range(start, stop, stepsize)

#using for loop
num = range(4,9,2)
for i in num:
	print(i)

print()

#using while loop
num2 = range(5,10,2)
i=0
while i<len(num2):
	print(num2[i])
	i=i+1

print()

#using list() and range()
lst = list(range(1,5))
print(lst)
