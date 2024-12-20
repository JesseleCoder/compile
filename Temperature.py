import customtkinter as ctk


def grid_s(R,C,root):
  for i in range(R):
    root.grid_rowconfigure(i, weight=1)
  for i in range(C):
    root.grid_columnconfigure(i, weight=1)
#im a fucking idoit

def setup(root):
    root.title("Temperature Converter")
    root.geometry("400x400")
    root.resizable(False, False)
    for o in root.winfo_children():
        o.destroy()
    grid_s(5,5,root)
    textbox = ctk.CTkEntry(root, width=150, height=25, border_width=2, corner_radius=5)
    textbox.grid(row=0, column=0, columnspan=5)

  
    swich = ctk.CTkSwitch(root, text="ON IS C OFF IS F",onvalue="F", offvalue="C")
    swich.grid(row=2, column=0, columnspan=5)
    swich.select()
    def on_convert():
        try:
            temp_value = float(textbox.get())
            converted_temp = Temperature(temp_value, swich.get())
            if converted_temp is not None:
                print(f"Converted Temperature: {converted_temp}")
        except ValueError:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Error", "Please enter a valid number RETARD")
    
    run = ctk.CTkButton(root, text="Convert", command=on_convert)
    run.grid(row=1, column=0, columnspan=5)


def Temperature(Temp,Unit):
    import tkinter.messagebox as messagebox
    result = None
    unit_to = ""
    if Unit == "C":
        result = (Temp * 9/5) + 32
        unit_to = "F°"
    elif Unit == "F":
        result = (Temp - 32) * 5/9
        unit_to = "C°"
    if result is not None:
        messagebox.showinfo("Conversion Result", f"{round(result, 2)} {unit_to}")
#ultrakill is good game