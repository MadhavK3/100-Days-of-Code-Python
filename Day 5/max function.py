student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 178, 65, 89, 86, 55, 91, 64, 89]
print(sum(student_scores))
maxi = 0
for score in student_scores:
    if maxi < score:
        maxi = score
print(f" Maximum Score is {maxi}")


