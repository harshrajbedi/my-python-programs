lst = []
print('How many elements: ', end='')
n = int(input())

for i in range(n):
	print('Enter Elements of List: ', end='')
	lst.append(int(input()))

print(lst)

big = lst[0]
small = lst[0]

for i in range(1,n):
	if lst[i]>big: big=lst[i]
	if lst[i]<small: small=lst[i]

print('small = ',small)
print('big = ',big)