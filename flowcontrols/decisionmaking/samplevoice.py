import random
import pyttsx3
engine = pyttsx3.init()
#with open("words.txt") as file:
F = open("ques.txt", "r")
a=random.choice(open("ques.txt","r").readline().split(","))
b=a.split("?")
print(b[0])
engine.say(b[0])
engine.runAndWait()
word=b[1]
c=len(b[1])
#print(c)
disp= "_ " * (c)
print(disp)
allowed_errors= 4
guesses =[]

done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end="")
        else:
            print("_",end="")
    print("")
    guess= input(f"allowed errors left{allowed_errors},next guess")
    print(guess)
    print(guesses)
    c=guesses.append(guess.lower())
    print(c)
