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

def change_bg_color():
    colors = ["alice blue", "khaki", "light blue", "misty rose", "lavender"]
    root.config(bg=random.choice(colors))

def change_font_color():
    colors = ["dark slate gray", "dark red", "indigo", "olive drab", "dark blue"]
    label_quote.config(fg=random.choice(colors))

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")
root.config(bg="alice blue")  

button_generate = tk.Button(root, text="Show Quote", command=show_quote, bg="sky blue", fg="black", font=("Arial", 12, "bold"))
button_generate.pack(pady=10)

label_quote = tk.Label(root, text="", wraplength=400, font=("Arial", 14, "italic"), justify="center", bg="alice blue", fg="dark slate gray")
label_quote.pack(pady=20)

button_bg_color = tk.Button(root, text="Change Background Color", command=change_bg_color, bg="peach puff", fg="black", font=("Arial", 10))
button_bg_color.pack(pady=5)

button_font_color = tk.Button(root, text="Change Font Color", command=change_font_color, bg="misty rose", fg="black", font=("Arial", 10))
button_font_color.pack(pady=5)

root.mainloop()
