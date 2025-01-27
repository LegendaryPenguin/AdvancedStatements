class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]


student_results = []
for student in students:
    student_results.append(f'{student.name} Passed') if student.score >= 0.7 else student_results.append (f"{student.name} Failed")

map_results = list(map(lambda student: (f'{student.name} Passed') if student.score >= 0.7 else (f"{student.name} Failed"), students))

print (student_results)
print (map_results)


numbers = [1,2,3,4,5]
map_multiplication = list (map(lambda x: x *2, numbers))
print (map_multiplication)


failing_students = []
# for student in students:
#     if student.score < 0.7:
#         failing_students.append(student)
# print (failing_students)

filter_list = list(filter(lambda student: student.score < 0.7, students))
print (filter_list)

number = [1,2,3,4,5]
filter_numbers = list(filter(lambda number: number %2 == 0, numbers))
print (filter_numbers)


score_total = 0
for student in students:
    score_total += student.score
print (score_total/ len(students))

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)
print (round(reduce_total/len(students), 2))

reduce_numbers = reduce(lambda total, number: number * total, number, 1)
print (reduce_numbers)