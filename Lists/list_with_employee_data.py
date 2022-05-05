emp = []
n = int(input('How many Employees: '))

for i in range(n):
	print('Enter Employee ID: ',end='')
	emp.append(int(input()))
	print('Enter Employee Name: ',end='')
	emp.append(input())
	print('Enter Employee Salary: ',end='')
	emp.append(float(input()))


id = int(input('Enter the ID to search: '))

for i in range(len(emp)):
	if id==emp[i]:
		print('ID = {:d}, Name = {:s}, Salary = {:.2f}'.format(emp[i], emp[i+1], emp[i+2]))
		break