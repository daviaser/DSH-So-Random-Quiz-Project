#Randon Questions Quiz Program
import random 
from quiz_questions import questions, answers

score = 0
total = 0
end = ''
used_list = []

print("Welcome to the So Random Quiz! Let's Play!")
while (end != "no"):
    f = random.choice(questions)
    if f not in used_list:
        print("")
        print(f)
        used_list.append(f)
        total +=1
        q = questions.index(f)
        a = answers[q]
        answer = input("Your answer: ")
        if answer.lower() == a.lower():
            print('\nYes! Your answer is Correct!')
            score = score + 1
            print("Your score is: " + str(score))
            print("")
            print("")
        else:
            print("\nSorry! That is incorrect.")
            print("The answer is : " + str(a))
            print("Your score is: " + str(score))
            print("")
            print("")
        end = input("Do you want to continue? ").lower()
    else:
        pass
        
    
    if (end=="no") and (score == total):
        print("Your final score is: " + str(score) + " and you answered a total of "+ str(total) +" questions! Perfect Score! Excellent Job!")
    elif end == "no":
        print("Your final score is: " + str(score) + ", and you answered a total of "+ str(total) +" questions! Congrats!")
