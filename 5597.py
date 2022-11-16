student = []
for i in range(30) :
    student.append(i+1)

for i in range(28) :
    num = int(input())
    student.remove(num)
print(student[0])
print(student[1])