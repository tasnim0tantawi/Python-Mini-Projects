from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km_output.config( text=str(miles * 1.60934))


window = Tk()
window.title("Miles to KM Converter")
window.config( padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)
km_output = Label(text="0")
km_output.grid(row=1, column=1)
km_label = Label(text="KM")
km_label.grid(row=1, column=2)
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)



window.mainloop()