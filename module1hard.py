grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_students = sorted(students)
student_grades = dict(zip(sort_students, grades))
print(student_grades)


Aaron = 'Aaron'
Bilbo = 'Bilbo'
Johhny = 'Johhny'
Khendrik = 'Khendrik'
Steve = 'Steve'

for Aaron in input():
    print('Aaron: ', sum(grades[0]) / len(grades[0]))
    break
for Bilbo in input():
    print('Bilbo: ', sum(grades[1]) / len(grades[1]))
    break
for Johhny in input():
    print('Johhny: ', sum(grades[2]) / len(grades[2]))
    break
for Khendrik in input():
    print('Khendrik: ', sum(grades[3]) / len(grades[3]))
    break
for Steve in input():
    print('Steve: ', sum(grades[4]) / len(grades[4]))
    break


