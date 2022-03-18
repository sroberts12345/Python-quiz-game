#TechWIthTim 5 Mini Python Projects video
#Project #1 - Quiz Game
#https://www.youtube.com/watch?v=DLn3jOsNRVE


print("Welcome to my computer quiz")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    print("Exiting...")
    quit()

print("Ok, let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
    print("The correct answer was: central processing unit")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
    print("The correct answer was: Graphics Processing Unit")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
    print("The correct answer was: Random Access Memory")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")
    print("The correct answer was: Power Supply Unit")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "% of questions correct!")
print("Thanks for playing!")