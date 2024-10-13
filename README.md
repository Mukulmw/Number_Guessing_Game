

# Number Guessing Game

This project is a simple **Number Guessing Game** implemented in Python. The game generates a random number between 1 and 100, and the player has to guess the number within a limited number of attempts. The player can choose between two difficulty levels, `Hard` or `Easy`, which determine how many attempts they get.

## Features
- Random number generation between 1 and 100.
- Two difficulty levels:
  - **Hard**: 5 attempts.
  - **Easy**: 10 attempts.
- Player receives feedback after each guess, either "Too High", "Too Low", or "That's correct!" if the guess is right.
- The game ends when the player guesses correctly or runs out of attempts.

## How to Play
1. Run the Python script.
2. Choose a difficulty level (`Hard` or `Easy`).
3. Make a guess by entering a number between 1 and 100.
4. Receive feedback based on your guess:
   - "Too High" if your guess is higher than the number.
   - "Too Low" if your guess is lower than the number.
   - "That's correct!" if you guessed the number correctly.
5. The game ends when you either guess the correct number or run out of attempts.

## Requirements
- Python 3.x
- No additional external libraries are required beyond Python's standard library.

## How to Run the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
   ```
2. Navigate into the project directory:
   ```bash
   cd number-guessing-game
   ```
3. Run the script:
   ```bash
   python number_guessing_game.py
   ```

## Example Gameplay

```
Choose the difficulty, Hard or Easy: easy
Make a guess you have 10 left !: 50
Too High
Make a guess you have 9 left !: 25
Too Low
Make a guess you have 8 left !: 37
That's correct!
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.