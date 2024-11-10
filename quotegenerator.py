import tkinter as tk
import random

quotes = [
    "Believe in yourself!",
    "Stay positive and happy.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

def show_quote():
    quote = random.choice(quotes)
    label_quote.config(text=quote)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x200")

label_quote = tk.Label(root, text="", wraplength=300, font=("Arial", 12), justify="center")
label_quote.pack(pady=20)

button_generate = tk.Button(root, text="Show Quote", command=show_quote)
button_generate.pack(pady=10)

root.mainloop()
