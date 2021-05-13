def swap(lst):
    size = len(lst)

    temp = lst[0]
    lst[0] = lst[size - 1]
    lst [size - 1] = temp
     
    return lst

lst = []
n = int(input("Enter number of elements in the list: "))

print("Start entering the elements")

for i in range (0,n):
    elements = int(input())

    lst.append(elements)

print(swap(lst))