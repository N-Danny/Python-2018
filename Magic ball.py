import random
import time
import sys

Start = input("Would you like to play? ")

if Start == "yes":
    name = input("Please enter your name. ")
    time.sleep(1)
    sys.exit

else:
    if Start == "no":
        print("Goodbye!")
        time.sleep(1)
        sys.exit()

print("When you are done asking questions please enter 'I am done'")
print("Give it a moment. Will be with you soon")


questions = ""
answers = ["No, %s " %name, "Unknown, %s" %name, "hell yeah, %s" %name, "You won't, %s" %name,]

time.sleep(5)

while questions != "I am done":
    questions = input("Ask your question. ")
    print(random.choice(answers))
    if questions == "I am done":
        break
sys.exit()