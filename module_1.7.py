grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_new = [sum(grades[0])/len(grades[0]), sum(grades[1]) / len(grades[1]),
              sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
              sum(grades[4])/len(grades[4])]
print(grades_new)
student_new = sorted(students)
print(student_new)
s = dict(zip(student_new, grades_new))
print(s)