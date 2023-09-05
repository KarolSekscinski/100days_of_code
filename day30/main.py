from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_flashcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = r.choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(translation, text=french_word, fill="black")
    canvas.itemconfig(canvas_card, image=card_front_img)
    flip_timer = window.after(3000, func=flip_flashcard)


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_flashcard()


def flip_flashcard():
    global current_card
    english_word = current_card['English']
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(translation, text=english_word, fill="white")
    canvas.itemconfig(canvas_card, image=card_back_img)


# UI
# Window
window = Tk()
window.title("Flashy cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_flashcard)
# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
translation = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_flashcard)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)
new_flashcard()

window.mainloop()
