import random
import time
import sys

rnum = random.randint(0, 100)

print("You got", str(rnum) + "%")

for i in range(rnum):
    sys.stdout.write("\r" + "\033[92m#" * i + "\033[0m." * (100-i))
    sys.stdout.flush()
    time.sleep(0.05)

if rnum == 100:
    print("\nFINALLY! You achieved 'Inner peace...'")
elif rnum > 90:
    print("\nYou're almost complete!")
elif rnum > 70:
    print("\nMore than half way there!")
elif rnum > 50:
    print("\nHalf way there!")
elif rnum > 30:
    print("\nSlightly up!")
elif rnum > 0:
    print("\nJust getting started!")
else:
    print("\033[91m\033[1m Uh oh...")


#So this program currently generate a random number
#Displays the percentage as text
#Then also as a progress bar
#I learned how to change its color in the shell, amazing.
#I also added text at the bottom that changes depending on where you are on the line