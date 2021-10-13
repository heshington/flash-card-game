from tkinter import *
from random import choice, randint, shuffle
import pandas

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}
# ---------------------------- READ CSV ------------------------------- #


try:
    df = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('./data/french_words.csv')
finally:
    to_learn = df.to_dict(orient='records')
    print(to_learn)


# ---------------------------- CARD CODE ------------------------------- #
def next_card():
    global CURRENT_CARD
    canvas.itemconfig(displayed_card, image=card_front)
    CURRENT_CARD = choice(to_learn)
    print(CURRENT_CARD)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=CURRENT_CARD['French'], fill="black")
    window.after(3000, card_flip)


def card_flip():
    global CURRENT_CARD
    canvas.itemconfig(displayed_card, image=card_back)
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=CURRENT_CARD['English'], fill="white")


def remove_card():
    to_learn.remove(CURRENT_CARD)
    print(len(to_learn))
    to_learn_data_frame = pandas.DataFrame(to_learn)
    to_learn_data_frame.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
displayed_card = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# canvas text
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 40, "bold"))
# buttons

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=remove_card)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()
