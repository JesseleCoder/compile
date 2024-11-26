import random
import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("BINGO_TEST_01")
root.geometry("400x450")
root.resizable(False, False)
picked_number = []

card = [[0, 0, 0, 0, 0] for _ in range(5)]

def Card_Data_Change(Row, Column, data):
    card[Row][Column] = data
    print(f"Row:{Row} Column:{Column} data:{data}")

def Gen_row(row):
    for col in range(5):
        card[row][col] = random.randint(1, 15)

def Gen_card():
    for row_index in range(5):
        Gen_row(row_index)
    Card_Data_Change(2, 2, 0)

Gen_card()

def pick_number():
    number = random.randint(1, 15)
    if number not in picked_number:
        messagebox.showinfo("BINGO", f"The number is {number}")
        picked_number.append(number)

# Create the Bingo grid (5x5)
for row in range(5):
    for col in range(5):
        value = card[row][col]
        label = tk.Label(root, text=str(value), width=5, height=2, borderwidth=2, relief="solid")
        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Add button below the Bingo grid
button = tk.Button(root, text="Pick Number", command=pick_number)
button.grid(row=5, column=0, columnspan=5, pady=10)

# Configure all rows and columns to have equal weight, including row 5 (button's row)
for i in range(6):  # Now also include row 5
    root.grid_rowconfigure(i, weight=1, minsize=50)

for i in range(5):  # Configure columns
    root.grid_columnconfigure(i, weight=1, minsize=50)

root.mainloop()
