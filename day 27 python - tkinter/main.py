from tkinter import *
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=5, pady=20)

# label = Label(text="Miles To KM Converter", font=("Arial, 20"))
# label.grid(column=0, row=0)

input = Entry(width=10)
input.grid(column=0, row=1,sticky="w", padx=0, pady=5)
input.insert(END,string="0")

miles_label = Label(text="Miles")
miles_label.grid(column="1", row="1")
is_equal_label = Label(text="Is Equal To: ")
is_equal_label.grid(column="2", row="1")
km_result_label = Label(text="0")
km_result_label.grid(column="3", row="1")
km_label = Label(text="Kilometers")
km_label.grid(column="4", row="1")


def clickbutton():
    miles = float(input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

button = Button(text="Calculate", command=clickbutton)
# button.pack()
button.grid(column=2,row=2, sticky="w", padx=10, pady=5)

window.mainloop()