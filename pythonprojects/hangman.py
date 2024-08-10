import random 

words = ['family feud', 'price is right', 'jeopardy', 'wheel of fortune', 'survivor']

# Randomly choose a word from the list

chosen_word = random.choice(words)
word_display = ['_ ' for _ in chosen_word] #Create a list of underscores
attempts = 10 # Number of allowed attemps

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("\n""Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveals the letter guessed
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1
        
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(''.join(word_display))
    print("You survived!")
else:
    print("Sorry you have run out of attempts. The word was: " + chosen_word)
    print("You lost!")
    
