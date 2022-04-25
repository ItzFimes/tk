
print("Importing modules")

print("Importing time")
import time
time.sleep(1)
print("Importing all of tkinter modules and tkinter")
import tkinter
import tk
import _tkinter
from tkinter import *
from tkinter import messagebox
time.sleep(0.5)

print("Importing all of pygame modules and pygame")
import pygame
from pygame.constants import *
from pygame.cursors import *
time.sleep(0.5)
print("Importing os and os.path")
from os import path
time.sleep(1)
print("Checking paths and files")
import os.path
from os import path

p1 = ((path.exists('os\Boot')))
p2 = ((path.exists('os\Boot\Boot.py')))
p3 = ((path.exists('os')))
print(p1)
print(p2)
print(p3)
if p1 == False:
    print("Boot folder is missing. Cannot boot.")
if p2 == False:
    print("Boot file not found")
    udbloop = True
    udb = input("Do you want to boot with command @{default}(default boot)[Y/N]")
    while udbloop == True:
        if udb == "Y":
            print("Please wait...")
            print("Booting...")
            break
        if udb == "N":
            print("Please wait...")
            nb = input("Do you want to create a new boot file?[Y/N]")
            nbloop = True
            while nbloop:
                if nb  == "Y":
                    print("Creating new file...")
                    print("Please wait...")
                    f = open("os\Boot\Boot.gosboot", "w+")
                    f.write("@{default}")
                    f.close()
                    udbloop = False
                    
                    nbloop = False 
                    break
                if nb == "N":
                    print("Cannot boot")
                    input("Press enter to exit")
                    exit()
                else:
                    nb = input("Do you want to create a new boot file?[Y/N]")
        else:
            udb = input("Do you want to boot with command @{default}(default boot)[Y/N]")
print("All important files founded")
time.sleep(2)
print("Preparing tkinter and pygame")
pygame.init()
time.sleep(0.5)
print("Loading settings")
settings1 = open("os\default\defaultboot\Fastboot.py","r")
s1 = settings1.read()
if s1 == "Fastboot = False":
    print(s1)
    
if s1 == "Fastboot = True":
    print(s1)
    print("Preparing os for fast boot")
    print("Fast boot is not finished yet")
print("Starting VM based OS")
print("Booting")
time.sleep(1)
b = Tk()
b.title("BOOTING")
b.geometry("1200x1200")
b.config(background="black")
#
# Boot Img
boot1 = Canvas(b, width =800, height =600)      
boot1.place(x=300,y=70)
boot1IMG = PhotoImage(file="os\Boot\Bootimg\BootImg.png")    
boot1.create_image(0,0, anchor=NW, image=boot1IMG)
b.attributes("-fullscreen", True)
bootloop = 0

b.mainloop()
time.sleep(1)
b.destroy()
l = Tk()
l.geometry("1200x1200")
l.title("LOGIN")
l.attributes("-fullscreen", True)
l.mainloop()
