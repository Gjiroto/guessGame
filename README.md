## **Guessing Game**

A simple but fun number guessing game built with Python and Tkinter.

**How to Play**

1. The computer generates a random number between 1 and 100.
2. You have 3 attempts to guess the correct number.
3. After each guess, the game will provide a hint (whether your guess is too high or too low).
If you guess correctly, you win!
4.How to Run

**1- Prerequisites:**

    Python 3 (https://www.python.org/downloads/)
**2- Installation:**

Install Tkinter (Python 3.x): If you're using Python 3.x, tkinter should be included in the standard library. However, on some systems, it might not be installed by default. You can install it using the package manager for your system. For example, on Ubuntu, you can use sudo apt-get install python3-tk.

Install Tkinter (Python 2.x): If you're using Python 2.x, tkinter is known as Tkinter. You can install it using the package manager for your system. For example, on Ubuntu, you can use sudo apt-get install python-tk.

**3- Running the Game:**

 - Open a terminal or command prompt.
 - Navigate to the directory where you saved the main.py and interface.py files.
 - Execute the command: python main.py

**Game Interface**

 - Guess Entry: Enter your guess in this field.
 - Verify Button: Click this button to check your guess.
 - Result Label: Displays the outcome of your guess ("¡VICTORY!", "Incorrect", etc.)
 - Indication Label: Provides hints after each guess ("too low", "too high").
 - Play Again Button: Starts a new game.
 - Exit Button: Closes the game window

**Code Structure**

**main.py:**
 * Initializes the game.
 * Imports the interface functions.

**interface.py:**
 - Defines the Tkinter GUI elements (labels, buttons, entry fields).
 - Contains functions for:
 - Generating random numbers (generate_random_number)
 - Checking guesses (check_guess)
 - Resetting the game (play_again)

**Enjoy playing!**
