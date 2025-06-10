# grade= {
#     'A+': 91 -100,
#     'A' : 81-90,
#     'B+': 71-80,
#     'B' : 61-70,
#     'C+': 51-60,
#     'C' : 41-50,
#     'F' : below40,
# }

student_marks={
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem" : 34

}
student_grade={}

for student in student_marks: 
    marks=student_marks[student]
    if marks>90:
        student_grade[student]='A+'
    elif 90>=marks>=81:
        student_grade[student]='A'     
    elif 80>=marks>=71:
        student_grade[student]='B+'     
    elif 70>=marks>=61:
        student_grade[student]='B'     
    elif 60>=marks>=51:
        student_grade[student]='C+'     
    elif 50>=marks>=41:
        student_grade[student]='C'     
    if marks<=40:
        student_grade[student]='F'     
print(student_grade)
