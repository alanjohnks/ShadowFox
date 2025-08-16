import tkinter as tk
from tkinter import messagebox
import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]

WORD_BANK = [
    {"word": "python", "hint": "Popular programming language named after a comedy group."},
    {"word": "hangman", "hint": "You are playing it right now."},
    {"word": "encryption", "hint": "Turns plain text into cipher text."},
    {"word": "database", "hint": "Organized collection of information."},
    {"word": "algorithm", "hint": "A set of steps for solving a problem."},
    {"word": "variable", "hint": "A storage location paired with a name."},
    {"word": "function", "hint": "Block of code that runs when called."},
    {"word": "iterator", "hint": "Object that can be looped over."},
    {"word": "compiler", "hint": "Translates source code into machine code."},
    {"word": "debugging", "hint": "Finding and fixing software bugs."},
    {"word": "hardware", "hint": "The physical components of a computer."},
    {"word": "software", "hint": "Programs used by a computer."},
    {"word": "internet", "hint": "A global network of networks."},
    {"word": "protocol", "hint": "A set of rules for data exchange."},
    {"word": "binary", "hint": "Base-2 number system."},

    {"word": "photosynthesis", "hint": "Process plants use to make food."},
    {"word": "gravity", "hint": "Force that attracts objects toward Earth."},
    {"word": "atom", "hint": "Smallest unit of matter."},
    {"word": "evolution", "hint": "Process by which species change over time."},
    {"word": "galaxy", "hint": "A system of millions of stars."},

    {"word": "adventure", "hint": "An exciting or daring experience."},
    {"word": "mystery", "hint": "Something difficult to explain or understand."},
    {"word": "freedom", "hint": "The power to act as you choose."},
    {"word": "library", "hint": "A place with many books."},
    {"word": "whisper", "hint": "To speak very softly."},
    {"word": "friendship", "hint": "A close relationship between friends."},
    {"word": "journey", "hint": "An act of traveling from one place to another."},
    {"word": "courage", "hint": "The ability to face danger without fear."},
    {"word": "treasure", "hint": "Valuable items hidden or stored."},
    {"word": "ocean", "hint": "A vast body of salt water."},
    {"word": "mountain", "hint": "A large natural elevation of the earth."},
]


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game with Hints")

        self.word_data = random.choice(WORD_BANK)
        self.secret_word = self.word_data["word"]
        self.hint_text = self.word_data["hint"]
        self.guessed_letters = set()
        self.used_letters = set()
        self.lives_used = 0
        self.max_lives = len(HANGMAN_PICS) - 1
        self.hint_count = 0

        # Widgets
        self.canvas_label = tk.Label(master, text="", font=("Courier", 14), justify="left")
        self.canvas_label.pack()

        self.word_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.word_label.pack(pady=5)

        self.info_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.info_label.pack()

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=5)

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        self.guess_btn = tk.Button(btn_frame, text="Guess", command=self.guess)
        self.guess_btn.grid(row=0, column=0, padx=5)

        self.hint_btn = tk.Button(btn_frame, text="Get Hint", command=self.get_hint)
        self.hint_btn.grid(row=0, column=1, padx=5)

        self.update_display()

    def mask_word(self):
        return " ".join([ch if ch in self.guessed_letters else "_" for ch in self.secret_word])

    def update_display(self):
        self.canvas_label.config(text=HANGMAN_PICS[self.lives_used])
        self.word_label.config(text=self.mask_word())
        self.info_label.config(
            text=f"Lives left: {self.max_lives - self.lives_used} | Used letters: {', '.join(sorted(self.used_letters)) or '—'}"
        )

    def guess(self):
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha():
            messagebox.showwarning("Invalid", "Please enter letters only.")
            return

        # Full word guess
        if len(guess) > 1:
            if guess == self.secret_word:
                self.guessed_letters.update(self.secret_word)
                self.update_display()
                messagebox.showinfo("You Win!", f"Correct! The word was '{self.secret_word}'.")
                self.master.destroy()
            else:
                self.lives_used += 1
        else:  # Single letter
            if guess in self.used_letters:
                messagebox.showinfo("Duplicate", "You already guessed that letter.")
                return
            self.used_letters.add(guess)
            if guess in self.secret_word:
                self.guessed_letters.add(guess)
                if all(ch in self.guessed_letters for ch in self.secret_word):
                    self.update_display()
                    messagebox.showinfo("You Win!", f"The word was '{self.secret_word}'.")
                    self.master.destroy()
            else:
                self.lives_used += 1

        if self.lives_used >= self.max_lives:
            self.update_display()
            messagebox.showerror("Game Over", f"You lost! The word was '{self.secret_word}'.")
            self.master.destroy()
            return

        self.update_display()

    def get_hint(self):
        if self.hint_count == 0:
            messagebox.showinfo("Hint", self.hint_text)
        else:
            if self.lives_used < self.max_lives:
                self.lives_used += 1
                messagebox.showinfo("Extra Hint", f"{self.hint_text}\n\n(Cost: 1 life)")
            else:
                messagebox.showwarning("No Lives", "You have no lives left for a hint.")
        self.hint_count += 1
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
