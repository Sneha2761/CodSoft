import tkinter as tk
from tkinter import messagebox
import random

# Game Logic
def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize scores
user_score = 0
computer_score = 0

def play_round(user):
    global user_score, computer_score
    comp = computer_choice()
    result = determine_winner(user, comp)
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    messagebox.showinfo("Result", f"Your choice: {user}\nComputer's choice: {comp}\n{result}")
    update_scores()

def update_scores():
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create buttons for user choices
choices = ["rock", "paper", "scissors"]
for choice in choices:
    button = tk.Button(root, text=choice.capitalize(), font=("Arial", 15), command=lambda c=choice: play_round(c))
    button.pack(pady=10)

# Create a label to display scores
score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Arial", 15))
score_label.pack(pady=20)

# Create a button to reset the game
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 15), command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
