
import customtkinter as ctk
import time
import random

def setup(root):
  root.title("New GB Test")
  root.geometry("400x400")
  root.resizable(False, False)

  


  
  for o in root.winfo_children():
      if o == ctk.CTkButton(root):
        o.configure(fg_color="red")
        
  R, G, B = 255, 255, 255


  
  for i in range(255):
    R = min(255, R - 1)
    G = min(255, G - 1)
    B = min(255, B - 1)
    time.sleep(0.01)
    root.configure(fg_color=f'#{R:02x}{G:02x}{B:02x}')
    root.update()


  
  for i in range(255):
    R = min(255, R + 1)
    G = min(255, G + 1)
    B = min(255, B + 1)
    time.sleep(0.01)
    root.configure(fg_color=f'#{R:02x}{G:02x}{B:02x}')
    root.update()
    