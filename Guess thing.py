#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:58:14 2022

@author: priyankadas
"""



from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Random Password Guesser")

label = Label(root)
guessed_password = Entry(root)
guess = Label(root)


array_3d = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] , ["Heads", "Tails"] , ["A","B","C","D","E","F","G","H","I","J"]]]

def password1():
    r1 = random.randint(0,8)
    r2 = random.randint(0,1)
    r3 = random.randint(0,9)
    guess1 = guessed_password.get()
    password_stored = str(array_3d[0][0][r1]) + array_3d[0][1][r2] + array_3d[0][2][r3]
    if guess1 == password_stored:
        guess["text"] = "Your guess " + guess1
        label["text"] = "You guess right "   
    else:
        guess["text"] = "Your Guess " + guess1
        label["text"] = "The password " + password_stored
    
btn = Button(root, text = "Guess the Password", command = password1)
btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
guess.place(relx = 0.5, rely = 0.5, anchor = CENTER)
guessed_password.place(relx = 0.5, rely = 0.4, anchor = CENTER)
root.mainloop()