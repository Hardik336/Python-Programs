import pyautogui as s
import time

s.press("win")
# time.sleep(1)

s.write("whatsapp",interval=0.2)
s.press("enter")
# time.sleep(1)

# s.write("Hello, I am Hardik !!")
# s.press("enter")

# s.write("I am MCA student !!")
# s.press("enter")

"""Message Boxes
"""
# s.alert("This is alert box !!")
# s.confirm('Enter option.', buttons=['A', 'B', 'C'])
# s.prompt("What is your name ?")

# time.sleep(10)

im1=s.screenshot()
for i in range(1,11):
    time.sleep(1)
    im1.save(f"ScreenShot{i}.png")