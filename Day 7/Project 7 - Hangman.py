import random



stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["cat","dog","apple","banana","mango","chery","cricket","football","hockey"]
lives = 6
word = random.choice(word_list)
print(word)
length = len(word)
blank = ""
for i in range(0,length):
    blank+="_"
print(blank)

blank = list(blank)
blank_filled = 0
word = list(word)

while lives != 0 and blank_filled == 0:
    print(stages[lives])
    guess = input("Guess the word:  ")
    temp = 0
    for i in range(0,length):
        if guess == word[i]:
            blank[i] = guess
            word[i] = "_"
            temp = 1
            break


    if temp == 0:
        lives-=1
        print(f"Lost {6-lives} lives")

    print("".join(map(str,blank)))
    temp1 = 0
    for i in range(0,length):
        if blank[i] == "_":
            temp1+=1

    if temp1 == 0:
        blank_filled = 1
blank1 = ""
for i in range(0,length):
    blank1+=word[i]
if lives == 0:
    print(stages[0])
    print("*********   You Lost   *********\n*********   Game Over   *********")
if blank1 == "_"*length:
    print("*********   You Won   *********\n*********   Game Over   *********")
