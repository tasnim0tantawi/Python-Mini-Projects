import tkinter

window = tkinter.Tk()
window.title("My Window")

window.minsize(width=500, height=500)
# Labels
label1 = tkinter.Label(window, text="Hello World", font=("Arial", 20))
label1.pack()
label2 = tkinter.Label(window, text="Hello Tasnim", font=("Arial", 20))
label2.pack(side="left")

label1["text"] = "I am a label"


def click():
    print("I am a button")
    text = input.get()
    label2.config(text=text)


# Buttons
button1 = tkinter.Button(window, text="Click Me", command=click)
button1.pack()
# Entry

input = tkinter.Entry(width=20)
input.pack()
print(input.get())

window.mainloop()
