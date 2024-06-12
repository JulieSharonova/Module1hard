grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johhny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_students = sorted(students)
student_grades = dict(zip(sort_students, grades))
print(student_grades)

while 1 > 0:
    name = input('Name of student: ')
    if name == 'Aaron':
        print('Aaron: ', sum(grades[0]) / len(grades[0]))
    if name == 'Bilbo':
        print('Bilbo: ', sum(grades[1]) / len(grades[1]))
    if name == 'Johhny':
        print('Johhny: ', sum(grades[2]) / len(grades[2]))
    if name == 'Khendrik':
        print('Khendrik: ', sum(grades[3]) / len(grades[3]))
    if name == 'Steve':
        print('Steve: ', sum(grades[4]) / len(grades[4]))
