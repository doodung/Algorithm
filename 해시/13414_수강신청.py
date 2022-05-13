# 13414 수강신청
# 수강가능인원이 최종학생수보다 많을수도 있음 그래서 break 해야함
K, L = map(int, input().split())
student = {}
for _ in range(L):
    number = input()
    if number in student:
        del student[number]
        student[number] = 1
    else:
        student[number] = 1

student = list(student.keys())
a = 0
while a < K:
    if a >= len(student):
        break
    print(student[a])
    a += 1
