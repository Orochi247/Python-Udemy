import random
stages = ["Man Hanged", "Fifth Man", "Fourth Man", "Three Man", "Two Man", "One Man", "Zero Man"]
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#Todo-1 Create a "Placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#use a while loop to repeat the guessing option
game_over = False

correct_letters = []
#now checking lives of the player as per the hangman status starting from 6 and reducing as the player guesses a wrong word
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()

#Todo-2 Change For loop so that you keep the previous correct letter in the list 
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")
    
    if "_" not in display:
        game_over = True
        print("You win.")
        
    #print out ascii art(here just text to make it easy) as everytime user loses
    print(stages[lives])