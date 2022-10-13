from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
BACKGROUND_COLOR = '#b19bba'
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('500 german.csv')
    data = original_data.to_dict('records')
    to_learn = data
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="German", fill='#000000')
    canvas.itemconfig(word, text=current_card['German'], fill="#000000")
    canvas.itemconfig(background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill='#ffffff')
    canvas.itemconfig(word, text=current_card['English'], fill="#ffffff")
    canvas.itemconfig(background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flash Card German')
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(5000, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
background = canvas.create_image(400, 256, image=card_front_image)
title = canvas.create_text(400, 150, text='German', font=('Arial 20', 40, 'bold'))
word = canvas.create_text(400, 256, text='Word', font=('Arial 20', 60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file='images/wrong.png')
tick_image = PhotoImage(file='images/right.png')
cross_button = Button(image=cross_image, highlightthickness=0, background=BACKGROUND_COLOR, command=flip_card)
cross_button.grid(row=1, column=0)
tick_button = Button(image=tick_image, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
tick_button.grid(row=1, column=1)
next_card()

window.mainloop()