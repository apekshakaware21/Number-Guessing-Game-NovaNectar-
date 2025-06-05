import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Instructions
        self.label = tk.Label(
            master, 
            text="I'm thinking of a number between 1 and 100.\nCan you guess it?", 
            font=("Helvetica", 14), 
            justify="center"
        )
        self.label.pack(pady=15)

        # User input
        self.entry = tk.Entry(master, font=("Helvetica", 12), justify="center")
        self.entry.pack(pady=5)

        # Result
        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), fg="blue")
        self.result_label.pack(pady=10)

        # Buttons
        self.check_button = tk.Button(
            master, 
            text="Check My Guess", 
            command=self.check_guess, 
            font=("Helvetica", 12), 
            width=18
        )
        self.check_button.pack(pady=5)

        self.reset_button = tk.Button(
            master, 
            text="🔄 Start Over", 
            command=self.reset_game, 
            font=("Helvetica", 12), 
            width=18
        )
        self.reset_button.pack(pady=5)

        self.attempts_label = tk.Label(master, text="Attempts: 0", font=("Helvetica", 10), fg="grey")
        self.attempts_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().strip()
        if not guess.isdigit():
            self.result_label.config(text="⛔ Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < 1 or guess > 100:
            self.result_label.config(text="🚫 Number must be between 1 and 100.")
        elif guess < self.secret_number:
            self.result_label.config(text="🔻 Too low! Try a higher number.")
        elif guess > self.secret_number:
            self.result_label.config(text="🔺 Too high! Try a lower number.")
        else:
            self.result_label.config(text=f"🎉 Congratulations! You guessed it in {self.attempts} tries!")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="🔁 New game started! Make your guess.")
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
