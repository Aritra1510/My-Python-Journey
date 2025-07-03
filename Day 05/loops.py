student_scores = [150, 142, 185, 120, 171, 149, 24, 59, 68, 199, 78, 65, 89, 86, 165, 177, 173, 189, 169,69, 146]

# print(sum(student_scores))
sum = 0
for score in student_scores:
    sum += score
print("Total score:", sum)

# print(max(student_scores))
max = -1
for score in student_scores:
    if score > max :
        max = score
print(f"Highest score: {max}")

# sum1 = 0
# for number in range(1,101):
#     sum1 += number
# print(sum1)
