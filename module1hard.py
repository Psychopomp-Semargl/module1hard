grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = list(students)
students2.sort()
print(students2)

grades2 = []
s = 0
for i in grades:
    s = sum(i) / len(i)
    grades2.append(s)
print(grades2)

my_dict = dict(zip(students2, grades2))
print(my_dict)