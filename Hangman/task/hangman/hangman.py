import random

print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit:')
while True:
    if menu == "exit":
        break
    elif menu == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        predefined_word = list(random.choice(words))
        hidden_word = '-' * len(predefined_word)
        tries = position = counter = 0
        guessed_letter = []
        hidden_word = list(hidden_word)
        while True:
            print(f"\n\n{''.join(hidden_word)}")
            letter = input("Input a letter: ")
            if letter in guessed_letter:
                print("You've already guessed this letter")
                continue
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if letter.islower():
                guessed_letter.append(letter)
                if letter in predefined_word:
                    times = predefined_word.count(letter)
                    position = [i for i, x in enumerate(predefined_word) if x == letter]
                    index = 0
                    while index < times:
                        hidden_word[int(position[index])] = letter
                        index += 1
                else:
                    tries += 1
                    print("That letter doesn't appear in the word")
            else:
                print("Please enter a lowercase English letter")
        
            if tries == 8 or predefined_word == hidden_word:
                break
        print(f"You guessed the word!\nYou survived!" if predefined_word == hidden_word else "You lost!")
        break
  