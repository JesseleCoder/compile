import customtkinter as ctk
import pygame

try:
    pygame.mixer.init()
    has_audio = True
except pygame.error:
    has_audio = False

def setup(root):
    root.title("TASTE THE RAINBOW MOTHER FUCKER")
    root.geometry("400x400")
    root.resizable(False, False)
    for o in root.winfo_children():
        o.destroy()

    # Play audio if available

    
    while True:
        root.config(bg="red")
        root.update()
        root.config(bg="orange")
        root.update()
        root.config(bg="yellow")
        root.update()
        root.config(bg="green")
        root.update()
        root.config(bg="blue")
        root.update()
        root.config(bg="purple")
        root.update()
        
    