import keyboard
import time
import pyautogui
import subprocess
def a(a):
    keyboard.press_and_release(a)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
subprocess.Popen(r"C:\Program Files\Mozilla Firefox\firefox.exe")
time.sleep(1)
keyboard.write("discord.com/channels/@me", delay=0.02)
keyboard.press('enter')
time.sleep(10)
person = pyautogui.locateOnScreen('discord_account.png')
pyautogui.click(pyautogui.center(person,), interval=1)
keyboard.write("This message was not send by a human, a script did this --Mysterious Script", delay=0.02)
keyboard.press('enter')

