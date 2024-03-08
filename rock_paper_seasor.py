import tkinter as tk
import random
def determine_winner(user_choice, computer_choice):#winner find
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        update_scores("user")
        return "You win!"
    else:
        update_scores("computer")
        return "Computer wins!"
def update_scores(winner):#updating score
    if winner == "user":
        user_score_var.set(user_score_var.get() + 1)
    elif winner == "computer":
        computer_score_var.set(computer_score_var.get() + 1)
    update_scoreboard()
def update_scoreboard():
    scoreboard_label.config(text=f"User: {user_score_var.get()}  \nComputer: {computer_score_var.get()}")
def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
choices = ["rock", "paper", "scissors"]
user_score_var = tk.IntVar()
user_score_var.set(0)
computer_score_var = tk.IntVar()
computer_score_var.set(0)
scoreboard_labels = tk.Label(root, text="Scoreboard", font=("Arial", 16, "bold"))
scoreboard_labels.pack()
scoreboard_label = tk.Label(root, text=f"\nUser: {user_score_var.get()}  \nComputer: {computer_score_var.get()}", font=("Arial", 14))
scoreboard_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)
user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack()
def create_button(choice):
    button = tk.Button(root, text=choice.capitalize(), command=lambda c=choice: play_game(c))
    button.pack(pady=5)
for choice in choices:
    create_button(choice)
root.mainloop()
