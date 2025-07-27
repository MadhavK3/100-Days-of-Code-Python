maths_score = int(input("Enter The score of maths: "))
english_score = int(input("Enter The score of english: "))
if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
elif english_score >= 90:
    print("You're good at english")
else:
    print("You are Good at none")