# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You'll create a Hangman game where players guess letters to reveal a hidden word before running out of attempts. This assignment practices string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up Your Game Structure

#### Description

Start by setting up the basic structure of your Hangman game, including the word list and game variables.

#### Requirements

Your program should:

- Create a list of words that the game can randomly select from
- Initialize game variables for tracking the chosen word, guessed letters, and remaining attempts
- Display introductory messages to welcome the player
- Set up the game loop framework

### 🛠️ Implement Word Display and Guessing

#### Description

Build the core logic for accepting player guesses and displaying the current progress of the hidden word.

#### Requirements

Your program should:

- Display the word in progress with underscores for unguessed letters (e.g., `_ _ _ _`)
- Prompt the player to guess one letter at a time
- Check if the guessed letter is in the word
- Update the display to reveal correctly guessed letters
- Track all guessed letters to prevent duplicate guesses
- Display remaining attempts after each guess

### 🛠️ Add Game Flow and Win/Lose Conditions

#### Description

Complete the game by implementing logic for checking win/lose conditions and controlling the game flow.

#### Requirements

Your program should:

- Decrease the attempt counter only for incorrect guesses
- Check for win condition (all letters guessed)
- Check for lose condition (no attempts remaining)
- Display appropriate win or lose message at game end
- Ask the player if they want to play again
- Handle invalid input gracefully (non-alphabetic characters, duplicate guesses)
