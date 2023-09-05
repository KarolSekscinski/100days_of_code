from tkinter import *


def button_clicked():
    distance = round(float(text_input.get()) * 1.609344, 2)

    km_distance.config(text=f"{distance}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


text_input = Entry(width=10)
text_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_distance = Label(text="0")
km_distance.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()
