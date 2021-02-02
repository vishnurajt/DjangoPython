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
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors-=1
        if allowed_errors==0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done=False

if done:
    engine.say("you found the word!")
    print("Word is ",word)
    engine.runAndWait()
else:
    engine.say("Game over!he word was")
    print("Word is ", word)
    engine.runAndWait()