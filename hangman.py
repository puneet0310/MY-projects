import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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
 

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
end_of_game= False
number_of_letters= len(chosen_word)
display=[]
lives = 6
for i in range (0,number_of_letters):
    display +="_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()   
    for position in range(number_of_letters):
        letter= chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -=1    
        if lives ==0:
            end_of_game =True
            print("You lose!!")
            
    print(display)
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")
    print(stages[lives])
    