# Rock-Paper-Scissors Game

This is a simple **Rock-Paper-Scissors** game built using the Python `tkinter` library. It allows the user to play the classic game against the computer by selecting either Rock, Paper, or Scissors.

## Features

- **User Interaction**: The user can select Rock, Paper, or Scissors by clicking buttons.
- **Random Computer Choice**: The computer randomly selects Rock, Paper, or Scissors for each round.
- **Game Logic**: After the user makes a selection, the winner is determined based on the classic Rock-Paper-Scissors rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- **Result Display**: The result of each game is displayed using a message box showing both the user's and computer's choices, and whether the user won, lost, or tied.

## Requirements

- Python 3.x
- Tkinter (This is usually bundled with Python, but if not, you can install it with `pip install python-tk`)

## Code Explanation

The main file `rock_paper_scissors.py` contains the following components:

-   **Tkinter GUI**:
    -   A window with a title, label, and three buttons representing Rock, Paper, and Scissors.
    -   Each button is tied to the function `play_game()`, which is called with the respective user choice.
-   **Game Logic**:
    -   The function `play_game(user_choice)` compares the user’s choice with a randomly selected choice for the computer.
    -   The result is displayed using a message box.
-   **Result Display**:
    -   A message box shows whether the user won, lost, or tied after each game round.
