import tkinter as tk
from tkinter import messagebox
import random


def Think():
  user_input = Entry.get()
  if user_input == "":
    messagebox.showinfo("Error", "Please enter a question.")
  else:
   random_number = random.randint(1, 7)
   if random_number == 1:
    messagebox.showinfo("Answer", "It is certain.")
   if random_number == 2:
    messagebox.showinfo("answer", "It is decidedly so.")
   if random_number == 3:
    messagebox.showinfo("answer", "I Dont know.")
   if random_number == 4:
    messagebox.showinfo("answer", "I dont think so.")
   if random_number == 5:
    messagebox.showinfo("answer", "Dont Count on it")
   if random_number == 6:
    messagebox.showinfo("answer", "No")
   if random_number == 7:
    messagebox.showinfo("answer", "Yes")
   

root = tk.Tk()
root.title("8 ball")
root.geometry("200x100")
Label = tk.Label(root, text="What do you wish to know?")
Button = tk.Button(root, text="Ask", command=Think)
Entry = tk.Entry(root, show="")

user_input = Entry.get()



Label.pack()
Button.pack()
Entry.pack()

root.mainloop()
