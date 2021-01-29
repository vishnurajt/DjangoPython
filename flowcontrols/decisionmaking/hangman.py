

#with open("ques.txt", "r") as file:
 #   allText = file.read()
  #  quest = list(map(str, allText.split()))
   # print(random.choice(quest))
#F = open(“ques.txt”, ”r”)
#Print f
#print(random.choice(open("ques.txt","r").readline().split()))
#words = F.split()
#print(words)
import random
with open("words.txt") as file:
    words = file.readlines()
word = random.choice(words)[:]
#print(random.choice(word))

allowed_errors= 7
guesses =[]
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_",end=" ")
    print("")
    guess= input(f"allowed errors left{allowed_errors},next guess")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors ==0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done=False

if done:
    print(f"you found the word! it was {word}!")
else:
    print(f"Game over!he word was {word}")

