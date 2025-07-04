student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Exceeds Expectations"
    elif student_scores[i] > 71:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

print(student_grades)