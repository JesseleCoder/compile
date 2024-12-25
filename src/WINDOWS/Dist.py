import customtkinter as ctk
import tkinter.messagebox as messagebox


def grid_s(R,C,root):
  for i in range(R):
    root.grid_rowconfigure(i, weight=1)
  for i in range(C):
    root.grid_columnconfigure(i, weight=1)


#setup menu
def setup(root):
    root.title("Dist Converter")
    root.geometry("400x400")
    root.resizable(False, False)
    for o in root.winfo_children():
        o.destroy()
    grid_s(5,5,root)
    drop = ctk.CTkOptionMenu(root, values=["Miles", "Kilometers", "Yards", "Feet", "Inches", "Centimeters", "Meters", "AU", "Nanometers", "Picometers", "Observable Universe", "Planck Length", "Light Years", "Parsecs", "Nautical Miles", "Quarks", "Protons", "Neutrons", "Black Hole Earth Radius"])
    drop.grid(row=0, column=0, columnspan=5)

    drop_2 = ctk.CTkOptionMenu(root, values=["Miles", "Kilometers", "Yards", "Feet", "Inches", "Centimeters", "Meters", "AU", "Nanometers", "Picometers", "Observable Universe", "Planck Length", "Light Years", "Parsecs", "Nautical Miles", "Quarks", "Protons", "Neutrons", "Black Hole Earth Radius"])
    drop_2.grid(row=2, column=0, columnspan=5)
    textbox = ctk.CTkEntry(root, width=150, height=25, border_width=2,)
    textbox.grid(row=1, column=0, columnspan=5)

    button = ctk.CTkButton(root, text="Convert", command=lambda: convert(drop, drop_2, textbox))
    button.grid(row=1, column=5)


def convert_to_meter(num, unit):
    # Convert to meters based on the unit
    if unit == "Kilometers":
        num = float(num) * 1000  # 1 km = 1000 meters
    elif unit == "Meters":
        num = float(num)  # 1 meter = 1 meter (no change)
    elif unit == "Centimeters":
        num = float(num) / 100  # 1 cm = 0.01 meters
    elif unit == "Inches":
        num = float(num) * 0.0254  # 1 inch = 0.0254 meters
    elif unit == "Feet":
        num = float(num) * 0.3048  # 1 foot = 0.3048 meters
    elif unit == "AU":
        num = float(num) * 149597870.7 * 1000  # 1 AU = 149597870.7 kilometers -> convert to meters
    elif unit == "Nanometers":
        num = float(num) * 1e-9  # 1 nm = 1e-9 meters
    elif unit == "Picometers":
        num = float(num) * 1e-12  # 1 pm = 1e-12 meters
    elif unit == "Observable Universe":
        num = float(num) * 8.8e26  # Observable Universe diameter in meters
    elif unit == "Planck Length":
        num = float(num) * 1.616255e-35  # Planck Length in meters
    elif unit == "Light Years":
        num = float(num) * 9.461e15  # 1 light-year = 9.461e15 meters
    elif unit == "Parsecs":
        num = float(num) * 3.086e16  # 1 parsec = 3.086e16 meters
    elif unit == "Nautical Miles":
        num = float(num) * 1852  # 1 nautical mile = 1852 meters
    elif unit == "Quarks":
        num = float(num) * 1e-18  # Approximate size of a quark in meters
    elif unit == "Protons" or unit == "Neutrons":
        num = float(num) * 1.67e-15  # Approximate size of a proton/neutron in meters
    elif unit == "Black Hole Earth Radius":
        num = float(num) * 8.87e-3  # Schwarzschild radius in meters (approximate)
    elif unit == "Miles":
      num = float(num) * 1609.34  # 1 mile = 1609.34 meters
    else:
        print("Unknown unit!")
        return None  # If the unit is not recognized
    return num

def convert(From, To, num):
    try:
        dist = float(num.get())
        unit_from = From.get()
        unit_to = To.get()
        
        # Convert to meters first
        meter = convert_to_meter(dist, unit_from)
        if meter is None:
            return
            
        # Convert from meters to target unit
        result = None
        if unit_to == "Kilometers":
            result = meter / 1000
        elif unit_to == "Meters":
            result = meter
        elif unit_to == "Centimeters":
            result = meter * 100
        elif unit_to == "Inches":
            result = meter / 0.0254
        elif unit_to == "Feet":
            result = meter / 0.3048
        elif unit_to == "Yards":
            result = meter / 0.9144
        elif unit_to == "Miles":
            result = meter / 1609.34
        elif unit_to == "AU":
            result = (meter / 1000) / 149597870.7  # convert meters to kilometers and then to AU
        elif unit_to == "Nanometers":
            result = meter / 1e-9
        elif unit_to == "Picometers":
            result = meter / 1e-12
        elif unit_to == "Observable Universe":
            result = meter / 8.8e26
        elif unit_to == "Planck Length":
            result = meter / 1.616255e-35
        elif unit_to == "Light Years":
            result = meter / 9.461e15
        elif unit_to == "Parsecs":
            result = meter / 3.086e16
        elif unit_to == "Nautical Miles":
            result = meter / 1852
        elif unit_to == "Quarks":
            result = meter / 1e-18
        elif unit_to == "Protons" or unit_to == "Neutrons":
            result = meter / 1.67e-15
        elif unit_to == "Black Hole Earth Radius":
            result = meter / 8.87e-3
        
        if result is not None:
            messagebox.showinfo("Conversion Result", f"{round(result, 4)} {unit_to}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
  
  #f*ck off a
