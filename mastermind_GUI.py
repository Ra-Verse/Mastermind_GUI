import tkinter as tk
from tkinter import messagebox
import random

# Constants for colors
COLORS = ["R", "B", "Y", "O", "G", "W"]
COLOR_NAMES = {"R": "red", "B": "blue", "Y": "yellow", "O": "orange", "G": "green", "W": "white"}

# Function to generate the random code
def code_gen(code_length):
    code = []
    for i in range(code_length):
        code.append(random.choice(COLORS))
    return code

# Function to compare the user's guess and our random code
def check_code(guess, code):
    color_count = {}
    correct_position = 0
    incorrect_position = 0

    color_count = {}
    for color in code:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    correct_position = 0
    incorrect_position = 0

    for i in range(len(code)):
        if guess[i] == code[i]:
            correct_position += 1
            color_count[guess[i]] -= 1

    for i in range(len(code)):
        if guess[i] != code[i]:
            if guess[i] in color_count and color_count[guess[i]] > 0:
                incorrect_position += 1
                color_count[guess[i]] -= 1

    return correct_position, incorrect_position

# Main application class
class MastermindApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        self.root.geometry("800x800")
        self.root.config(bg="#000000")

        # Default values for tries and code length
        self.tries = 10
        self.code_length = 4
        self.code = code_gen(self.code_length)
        self.attempts_left = self.tries # as user has full amount of tries at the start
        self.attempts = []

        # creating all the UI elements
        self.game_frame = tk.Frame(root, bg="#151AC4", bd=15, relief="solid", padx=20, pady=20)
        self.game_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.game_frame, text="Mastermind", font=("Verdana", 30, "bold"), bg="#333333", fg="white").grid(row=0, columnspan=4, pady=10)

        self.attempt_label = tk.Label(self.game_frame, text=f"Attempts left: {self.attempts_left}", font=("Frozen", 16), bg="#333333", fg="white")
        self.attempt_label.grid(row=1, columnspan=4)

        self.settings_frame = tk.Frame(self.game_frame, bg="#333333")
        self.settings_frame.grid(row=2, columnspan=4, pady=20)

        self.tries_label = tk.Label(self.settings_frame, text="Tries:", font=("Verdana", 12), bg="#333333", fg="white")
        self.tries_label.grid(row=0, column=0, padx=20)

        self.tries_entry = tk.Entry(self.settings_frame, font=("Verdana", 12), bg="#444444", fg="white", insertbackground="white")
        self.tries_entry.grid(row=0, column=1, padx=20)
        self.tries_entry.insert(0, str(self.tries))

        self.code_length_label = tk.Label(self.settings_frame, text="Code Length:", font=("Verdana", 12), bg="#333333", fg="white")
        self.code_length_label.grid(row=1, column=0, padx=20)

        self.code_length_entry = tk.Entry(self.settings_frame, font=("Verdana", 12), bg="#444444", fg="white", insertbackground="white")
        self.code_length_entry.grid(row=1, column=1, padx=20)
        self.code_length_entry.insert(0, str(self.code_length))

        self.update_button = tk.Button(self.settings_frame, text="Update Settings", command=self.update_settings, font=("Verdana", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", width=20, borderwidth=1, highlightthickness=0)
        self.update_button.grid(row=2, columnspan=2, pady=10, padx=20)

        self.guess_frame = tk.Frame(self.game_frame, bg="#333333")
        self.guess_frame.grid(row=3, columnspan=4, pady=10)

        self.guess_vars = [tk.StringVar(value="W") for _ in range(self.code_length)]
        self.guess_buttons = []
        self.create_guess_buttons()

        tk.Button(self.game_frame, text="Submit Guess", command=self.submit_guess, font=("Verdana", 14, "bold"), bg="#2196F3", fg="white", relief="flat", width=20, borderwidth=1, highlightthickness=0).grid(row=4, columnspan=4, pady=20)

        self.history_frame = tk.Frame(self.game_frame, bg="#333333")
        self.history_frame.grid(row=5, columnspan=4, pady=20)

    # guess buttons
    def create_guess_buttons(self):
        for widget in self.guess_frame.winfo_children():
            widget.destroy()

        self.guess_vars = [tk.StringVar(value="W") for _ in range(self.code_length)]  # Reset the gues vars

        # new guess buttons
        self.guess_buttons = []
        for i in range(self.code_length):
            button = tk.Button(self.guess_frame, text=" ", width=5, height=2, relief="flat", bg="white", command=lambda i=i: self.change_guess_color(i))
            button.grid(row=0, column=i, padx=5)
            self.guess_buttons.append(button)  # Adds a new buttons to the list as it was cleared (line 109)

    # Function to update tries and code length
    def update_settings(self):
        try:
            new_tries = int(self.tries_entry.get())
            new_code_length = int(self.code_length_entry.get())

            if new_tries <= 0 or new_code_length <= 0:
                raise ValueError("Tries and Code Length must be positive integers.")

            self.tries = new_tries
            self.code_length = new_code_length
            self.attempts_left = self.tries
            self.attempts = []
            self.code = code_gen(self.code_length)

            self.attempt_label.config(text=f"Attempts left: {self.attempts_left}")
            self.create_guess_buttons()  # Create new buttons based on the new code length
            self.display_history()

            messagebox.showinfo("Settings Updated", "Game settings updated. You can now start a new game.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    # Function to handle color selection for guesses
    def change_guess_color(self, index):
        current_color = self.guess_vars[index].get()
        current_index = COLORS.index(current_color)
        next_index = (current_index + 1) % len(COLORS)  # Cycle through the colors
        new_color = COLORS[next_index]
        self.guess_vars[index].set(new_color)
        self.guess_buttons[index].config(bg=COLOR_NAMES[new_color])

    # Function to handle when a guess is submitted
    def submit_guess(self):
        guess = [var.get() for var in self.guess_vars]
        correct_position, incorrect_position = check_code(guess, self.code)

        self.attempts_left -= 1
        self.attempt_label.config(text=f"Attempts left: {self.attempts_left}")

        attempt_result = f"Guess: {' '.join(guess)} | Correct: {correct_position} | Incorrect: {incorrect_position}"
        self.attempts.append((guess, attempt_result))

        self.display_history()

        if correct_position == self.code_length:
            messagebox.showinfo("Game Over", f"You cracked the code in {self.tries - self.attempts_left} attempts!")
            self.root.quit()
        elif self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"You ran out of tries! The code was {' '.join(self.code)}")
            self.root.quit()

    # Function to display previous attempts with colored dots
    def display_history(self):
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        for guess, result in self.attempts:
            frame = tk.Frame(self.history_frame, bg="#333333")
            frame.pack(pady=5)

            for color in guess:
                dot = tk.Label(frame, bg=COLOR_NAMES[color], width=4, height=2, relief="flat", bd=2, highlightthickness=1, padx=3, pady=3)
                dot.pack(side="left", padx=8)

            result_label = tk.Label(frame, text=result, font=("Verdana", 10), width=40, anchor="w", bg="#333333", fg="white")
            result_label.pack(side="left", padx=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MastermindApp(root)
    root.mainloop()
