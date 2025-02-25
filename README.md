# Mastermind Game

This is a simple Mastermind game implemented in Python using Tkinter for the GUI.

## Features

-   **Customizable Settings:**
    -      Adjust the number of tries.
    -      Change the length of the secret code.
-   **Color-Coded Guesses:**
    -      Select colors for your guesses using interactive buttons.
    -      Visual feedback on the correctness of your guesses.
-   **Game History:**
    -      View your previous attempts with color-coded dots and feedback.
-   **User-Friendly Interface:**
    -      Clear and intuitive GUI using Tkinter.
    -   Displays the amount of attempts left.
-   **Game Over Messages:**
    -   Displays a message when you win or lose.

## How to Run

1.  **Prerequisites:**
    -      Python 3.x
    -      Tkinter (usually included with Python)

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Ra-Verse/Mastermind_GUI
    ```

3.  **Run the Script:**

    ```bash
    python mastermind_GUI.py
    ```

## How to Play

1.  **Settings:**
    -      Enter the desired number of tries and code length in the settings section.
    -      Click "Update Settings" to apply the changes.
2.  **Guessing:**
    -      Click the color buttons to cycle through the available colors.
    -      Once you've selected your guess, click "Submit Guess."
3.  **Feedback:**
    -      The game will provide feedback on your guess, indicating the number of correct colors in the correct positions and the number of correct colors in incorrect positions.
    -   Your guess and the results are displayed in the history section.
4.  **Winning/Losing:**
    -      The game ends when you correctly guess the code or run out of tries.
    -   A message box will display the result.

## Code Explanation

-   **`code_gen(code_length)`:** Generates a random code of the specified length using colors from the `COLORS` list.
-   **`check_code(guess, code)`:** Compares the user's guess with the secret code and returns the number of correct positions and incorrect positions.
-   **`MastermindApp` class:**
    -      Handles the GUI and game logic.
    -      Uses Tkinter to create the game interface.
    -      Provides methods for updating settings, handling guesses, and displaying game history.
-   **Tkinter:**
    -   The GUI is built using tkinter.
    -   Frames, Labels, Buttons, and Entries are used to create the game interface.
    -   Messagebox is used to display pop-up messages.

## Dependencies

-   `tkinter`
-   `random`
