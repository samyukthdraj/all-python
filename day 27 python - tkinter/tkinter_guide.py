###### import tkinter

###### window = tkinter.Tk()
###### window.title("GUI SDR")
###### window.minsize(width=500, height=300)

###### label = tkinter.Label(text="Label1", font=("Arial", 24, "italic"))
###### label.pack(side="left") #to make the label on the left of the screen
###### label["text"] = "New label" #replaces the label1 to new label

###### Create a new button
###### button = tkinter.Button(text="Click Me")
###### button.pack()

###### window.mainloop()

###this same code can be written without the Tk if we instead do from tkinter import *

from tkinter import *

#Tk(); creating a new screen
window = Tk()
window.title("GUI SDR")
window.minsize(width=500, height=300)

#Label(); giving the texts to a screen.
label = Label(text="Label1", font=("Arial", 24, "italic"))
label.pack() #to make the label on the center of the screen
label["text"] = "New label" #replaces the label1 to new label
label.config(text="New label") #does the same as previous line of code.

#clicking the button should do something
def buttonclick():
    new_text = input.get()
    label.config(text=new_text)
    print(new_text)

#Button(); Create a new button
button = Button(text="Click Me", command=buttonclick)
button.pack()

#Entry() ie: giving input
input = Entry(width = 15)
input.pack()
input.insert(END, string="Type something...") #starting text in an input field.
input.get() #print the text entered in the text input field.


#Text(); textbox
textbox = Text(height=5, width= 35)
textbox.focus() #puts the curson in the textbox
textbox.insert(END, "Enter something in this textbox.")
textbox.pack()
print(textbox.get("1.0",END))#getting from first character.

#Spinbox(); Click on the up and down arrow to add or minus
def spinboxused():
    print(spinbox.get())

spinbox = Spinbox(from_ = 0 , to = 10, width = 5,command= spinboxused)
spinbox.pack()

#Scale(); scale with a slider
def scaleused(value):
    print(value)

scale = Scale(from_=0, to=100,command=scaleused)
scale.pack()

#Checkbutton()
def checkbuttonused():
    print(checked_state.get()) #1 if on checked else 0

checked_state = IntVar() 
checkbutton = Checkbutton(text="ON?",variable=checked_state,command=checkbuttonused)
checked_state.get()
checkbutton.pack()

#RadioButton    
def radioused():
    print(radio_state.get())

radio_state= IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radioused)
radiobutton1.pack()

radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radioused)
radiobutton2.pack()

#Listbox()
def listboxused(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Pear"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listboxused)
listbox.pack()



window.mainloop()