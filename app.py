# MADLIBS 
# mini python project
# Cate Hazleden-Butler | Generation AU | AZC07 2023

#imported modules
import time,sys, os

#functions for the typing effect for output and input with the parameter of "text"
# references the sys module for standard output to write the character immediately after the current one and to flush forcing it to update immediately(without buffering)


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value

#function to clear screen
def clearScreen():
  os.system("clear")

#ADD INTRO AND RULES


#MadLib 1 input variables
verb1 = input("Verb: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
noun1 = input("Noun: ")
noun2 = input("Person's name: ")
adv1 = input("Adverb: ")
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")


#mad libs1 output variable using f string (formatted string literals)

madlib1 = f"At a(n) {adj1} tech firm, a {adj2} {noun1} chose to {verb1} in the break room. \nSuddenly, {noun2} {verb2} {adv1} in. \nThey exchanged a {adj3} nod & {verb3} excitedly about their projects. \nThe day became a {adj4} memory, showing work can have surprises!\n\n"


print("")
time.sleep(1)
typingPrint("Processing your Mad Lib! \n\n")
time.sleep(3)
typingPrint("boop, beep, boop \nStill processing...\n\n")
time.sleep(3)

typingPrint(madlib1)

time.sleep(2)


#goodbye sequence
goodbye = typingInput("Do you want to play again? (Type y or n)\n")

if goodbye == "y":
  typingPrint("Sorry, I don't have time today!\n")
elif goodbye == "n":
  typingPrint("You'll be back!\n")
else:
  typingPrint("Wrong answer!\n")

time.sleep(3)
typingPrint("Good bye!\n")
time.sleep(3)
typingPrint("This screen will clear itself in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()