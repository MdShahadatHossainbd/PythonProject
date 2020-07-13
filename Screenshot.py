# pip install pyautogui

import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.TK()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def take_screenshot():
    myScreenshot = pyautogui.screenshot()
    save_path = askopenfilename()
    myScreenshot.save(save_path+'screenshot.png')

myButton = tk.Button(text='Take screenshot', command = take_screenshot,font=10)
canvas1.create_window(150,150, window = myButton)
root.mainloop()