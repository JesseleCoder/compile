import customtkinter as ctk
from WINDOWS import Temperature as temp
from WINDOWS import RAINBOW as rain
from WINDOWS import Dist as dist
from WINDOWS import MASS as time8


root = ctk.CTk()
root.geometry("400x400")
root.title("CustomTkinter")

def setup(R,C):
  for i in range(R):
    root.grid_rowconfigure(i, weight=1)
  for i in range(C):
    root.grid_columnconfigure(i, weight=1)
setup(5,5)
    

lable = ctk.CTkLabel(root, text="Unit Converter")
lable.grid(row=0, column=2)


temp_button = ctk.CTkButton(root, text="Temperature", command=lambda: temp.setup(root))
temp_button.grid(row=0, column=2)

rain_button = ctk.CTkButton(root, text="Rainbow", command=lambda: rain.setup(root))
rain_button.grid(row=2, column=2)

dist_button = ctk.CTkButton(root, text="Distance", command=lambda: dist.setup(root))
dist_button.grid(row=1, column=2)

useless = ctk.CTkButton(root, text="Mass", command=lambda: time8.setup(root))
useless.grid(row=3, column=2)






root.mainloop()
