if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])

    second_lowest = students[1][1]
    print(second_lowest)

    required_students = []

    for std in students:
        if std[1] == second_lowest:
            required_students.append(std[0])
    print("\n".join((sorted(required_students))))