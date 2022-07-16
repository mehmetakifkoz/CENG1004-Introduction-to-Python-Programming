name    = input("Enter your name: ")
surname = input("Enter your surname: ")
age     = input("Enter your age: ")
gender  = input("Enter your gender(M/W): ")


# 1- Sensing / iNtuition
question1 = input("1- When you meet someone new, do you try to guess what they are like? ")
# 2- Judging / Perceiving
question2 = input("2- Do you get angry when your friends hurt you? ")
# 3- Thinking / Feeling
question3 = input("3- Are you a cold blooded person when you face some problems/troubles? ")
# 4- Extravert / Introvert
question4 = input("4- Are you the one who starts a conversation? ")


if   question1 == "yes" and question2 == "yes" and question3 == "yes" and question4 == "yes":
    result = "1. Extravert / Sensing / Thinking / Judging"
elif question1 == "yes" and question2 == "yes" and question3 == "yes" and question4 == "no" :
    result = "2. Introvert / Sensing / Thinking / Judging"
elif question1 == "yes" and question2 == "yes" and question3 == "no"  and question4 == "yes":
    result = "3. Extravert / Sensing / Feeling / Judging"
elif question1 == "yes" and question2 == "yes" and question3 == "no"  and question4 == "no" :
    result = "4. Introvert / Sensing / Feeling / Judging"
elif question1 == "yes" and question2 == "no"  and question3 == "yes" and question4 == "yes":
    result = "5. Extravert / Sensing / Thinking / Perceiving"
elif question1 == "yes" and question2 == "no"  and question3 == "yes" and question4 == "no" :
    result = "6. Introvert / Sensing / Thinking / Perceiving"
elif question1 == "yes" and question2 == "no"  and question3 == "no"  and question4 == "yes":
    result = "7. Extravert / Sensing / Feeling / Perceiving"
elif question1 == "yes" and question2 == "no"  and question3 == "no"  and question4 == "no" :
    result = "8. Introvert / Sensing / Feeling / Perceiving"
elif question1 == "no"  and question2 == "yes" and question3 == "yes" and question4 == "yes":
    result = "9. Extravert / iNtuition / Thinking / Judging"
elif question1 == "no"  and question2 == "yes" and question3 == "yes" and question4 == "no" :
    result = "10. Introvert / iNtuition / Thinking / Judging"
elif question1 == "no"  and question2 == "yes" and question3 == "no"  and question4 == "yes":
    result = "11. Extravert / iNtuition / Feeling / Judging"
elif question1 == "no"  and question2 == "yes" and question3 == "no"  and question4 == "no" :
    result = "12. Introvert / iNtuition / Feeling / Judging"
elif question1 == "no"  and question2 == "no"  and question3 == "yes" and question4 == "yes":
    result = "13. Extravert / iNtuition / Thinking / Perceiving"
elif question1 == "no"  and question2 == "no"  and question3 == "yes" and question4 == "no" :
    result = "14. Introvert / iNtuition / Thinking / Perceiving"
elif question1 == "no"  and question2 == "no"  and question3 == "no"  and question4 == "yes":
    result = "15. Extravert / iNtuition / Feeling / Perceiving"
elif question1 == "no"  and question2 == "no"  and question3 == "no"  and question4 == "no" :
    result = "16. Introvert / iNtuition / Feeling / Perceiving"


print(result)
rating = input("Please rate our questionnaire(1-10): ")
fhand = open("output.txt", "w", encoding="utf-8")
result_number = result.split('.')[0]
fhand.write(f"{name} {surname}, {age}, {gender}, {result_number}, {rating}")
fhand.close()
