exam = 1

for i in range(3):
    exam*=int(input())

exam = list(str(exam))

for j in range(10):
    print(exam.count(str(j)))