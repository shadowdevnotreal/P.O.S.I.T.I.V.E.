import random
from tkinter import Tk, Label, Button

# List of positive affirmations
affirmations = [
    "You are a radiant being, capable of achieving great things.",
    "Embrace your strengths and keep moving forward with confidence.",
    "You are worthy of love and respect, just as you are.",
    "Challenges are opportunities to learn and grow. You've got this!",
    "Believe in yourself and the power you hold to create a fulfilling life.",
    "Celebrate your progress, no matter how small. Every step counts.",
    "Your unique talents and skills make you special. Share them with the world!",
    "You are surrounded by love and support, even when it feels unseen.",
    "Remember, you are enough. You are worthy. You are loved.",
    "You are an inspiration to others. Keep shining your light!"
]

# Function to generate a random affirmation
def get_affirmation():
    return random.choice(affirmations)

# Function to display the affirmation and handle user input
def display_affirmation():
    # Create a GUI window
    window = Tk()
    window.title("Daily Affirmation")

    # Display the affirmation
    affirmation_label = Label(window, text=get_affirmation(), font=("Arial", 16))
    affirmation_label.pack(padx=20, pady=20)

    # Button to request a new affirmation
    new_affirmation_button = Button(window, text="New Affirmation", command=display_affirmation)
    new_affirmation_button.pack(pady=10)

    # Button to provide feedback (optional)
    # You can uncomment this block and add functionality to collect and store user feedback
    # feedback_button = Button(window, text="Share Feedback")
    # feedback_button.pack()

    window.mainloop()

# Run the program
display_affirmation()
