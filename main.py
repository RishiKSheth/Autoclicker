import pyautogui
import tkinter
from tkinter import ttk

#window tkinter
window = tkinter.Tk()
window.title("AutoClicker")
window.geometry("600x400")

#label for (1-100)
label = tkinter.Label(window, text = "(1-100) clicks per minute")
label.pack()

#Button to start the click


#drop down menu to select numbers 1-100
numbers = [str(i) for i in range(1, 101)]
selected_option = tkinter.StringVar()
dropdown = ttk.Combobox(window, textvariable=selected_option, values=numbers)
dropdown.pack(pady = 20)
window.mainloop()


