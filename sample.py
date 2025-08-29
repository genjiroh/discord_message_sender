import keyboard
import time
import subprocess
import re
import os
from plyer import notification
x = []
y = []
listen = False
message = "Script is not listening for commands. Press F4 to toggle on Listening Mode"
def search(filename):
    folders = [r"C:\Program Files", r"C:\Program Files (x86)", r"C:\Users\Shadow\AppData"]
    for folder in folders:
        x = os.walk(folder)
        for root, dirs, files in x:
            for file in files:
                if filename.lower() == file.lower():
                    path = os.path.join(root, file)
                    return path
    return None
def on_press(event):

    global y
    global listen
    global message
    print(y)
    if not listen:
        return       
    else:
        if event.name == "space":
            y.append(" ")
        elif event.name == "esc":
            exit()
        elif event.name == "backspace":
            if y:
                y.pop()
        elif event.name == "shift":
            pass
        elif event.name == "`":
            if listen == True:
                message = "Script is running and listening for commands. Press F4 to toggle off Listening Mode"
            else:
                message = "Script is not listening for commands. Press F4 to toggle on Listening Mode"
            notification.notify(title="Script Status", message=message, timeout=4)
        elif event.name == "enter":
            print(y)
            z = "".join(y)
            print(z)
            if "open" in z and listen == True:
                open_apps(z)
            if "shutdown" in z and listen == True:
                os.system("shutdown /sg /t 0")
            if "sign out" in z and listen == True:
                os.system("shutdown /l /t 0")
            if "restart" in z and listen == True:
                os.system("shutdown /g /t 0")
            if "discord" in z and listen == True:
                keyboard.press("ctrl+t")
                keyboard.write("discord.com/channels/@me", delay=0.04)
                keyboard.press('enter')
            if "youtube" in z and listen == True:
                keyboard.press('ctrl+t')
                print(z)
                keyboard.write("youtube.com", delay=0.04)
                keyboard.press('enter')
            y = []
            z = ""
            
        elif len(event.name) == 1:
            y.append(event.name)
def toggle_listen():
    global listen
    if listen == True:
        listen = False
    else:
        listen = True
keyboard.add_hotkey("f4", toggle_listen)



def open_apps(z):
    global y
    output = re.findall(r"open (\w+)", z, re.IGNORECASE)
    if output:
        output = output[0] + ".exe"
        filename = output
        path = search(filename)
        print(path)
        try:
            if path:
                subprocess.Popen(path, shell=True)
        except:
            print(f"Couldnt open the program you were looking for")
        z = ""
        y = []
        output = []

keyboard.on_press(on_press)
keyboard.wait('f12')