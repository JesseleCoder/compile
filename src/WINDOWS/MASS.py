import customtkinter as ctk
import tkinter.messagebox as messagebox


def grid_s(R,C,root):
  for i in range(R):
    root.grid_rowconfigure(i, weight=1)
  for i in range(C):
    root.grid_columnconfigure(i, weight=1)


#setup menu
def setup(root):
    root.title("Mass Converter")
    root.geometry("400x400")
    root.resizable(False, False)
    for o in root.winfo_children():
        o.destroy()
    grid_s(5,5,root)
    drop = ctk.CTkOptionMenu(root, values=["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces", "Tons", "Metric Tons", "Stone", "Quintals", "Atomic Mass Unit"])
    drop.grid(row=0, column=0, columnspan=5)

    drop_2 = ctk.CTkOptionMenu(root, values=["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces", "Tons", "Metric Tons", "Stone", "Quintals", "Atomic Mass Unit"])
    drop_2.grid(row=2, column=0, columnspan=5)
    textbox = ctk.CTkEntry(root, width=150, height=25, border_width=2,)
    textbox.grid(row=1, column=0, columnspan=5)

    button = ctk.CTkButton(root, text="Convert", command=lambda: convert(drop, drop_2, textbox))
    button.grid(row=1, column=5)


def convert_to_kg(num, unit):
    # Convert to kilograms based on the unit
    if unit == "Grams":
        num = float(num) / 1000  # 1 gram = 0.001 kilograms
    elif unit == "Milligrams":
        num = float(num) / 1e6  # 1 milligram = 0.000001 kilograms
    elif unit == "Pounds":
        num = float(num) * 0.453592  # 1 pound = 0.453592 kilograms
    elif unit == "Ounces":
        num = float(num) * 0.0283495  # 1 ounce = 0.0283495 kilograms
    elif unit == "Tons":
        num = float(num) * 907.185  # 1 ton = 907.185 kilograms
    elif unit == "Metric Tons":
        num = float(num) * 1000  # 1 metric ton = 1000 kilograms
    elif unit == "Stone":
        num = float(num) * 6.35029  # 1 stone = 6.35029 kilograms
    elif unit == "Quintals":
        num = float(num) * 100  # 1 quintal = 100 kilograms
    elif unit == "Atomic Mass Unit":
        num = float(num) * 1.66053906660e-27  # 1 amu = 1.66053906660e-27 kg
    elif unit == "Kilograms":
        num = float(num)  # 1 kilogram = 1 kilogram (no change)
    else:
        print("Unknown unit!")
        return None  # If the unit is not recognized
    return num

def convert(From, To, num):
    try:
        mass = float(num.get())
        unit_from = From.get()
        unit_to = To.get()

        # Convert to kilograms first
        kg = convert_to_kg(mass, unit_from)
        if kg is None:
            return

        # Convert from kilograms to target unit
        result = None
        if unit_to == "Grams":
            result = kg * 1000
        elif unit_to == "Milligrams":
            result = kg * 1e6
        elif unit_to == "Pounds":
            result = kg / 0.453592
        elif unit_to == "Ounces":
            result = kg / 0.0283495
        elif unit_to == "Tons":
            result = kg / 907.185
        elif unit_to == "Metric Tons":
            result = kg / 1000
        elif unit_to == "Stone":
            result = kg / 6.35029
        elif unit_to == "Quintals":
            result = kg / 100
        elif unit_to == "Atomic Mass Unit":
            result = kg / 1.66053906660e-27
        elif unit_to == "Kilograms":
            result = kg

        if result is not None:
            messagebox.showinfo("Conversion Result", f"{round(result, 4)} {unit_to}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

  #f*ck off a
