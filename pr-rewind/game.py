import lcdDisplay as lcd
import gpiozero as GPIO
import time
import joystick
import constants as con

row1 = ["","|"]
row2 = ["","|"]
msg1 = ""
msg2 = ""
position = 0
hit = False
hitpos = 0

btn = GPIO.Button(con.BTN, bounce_time = 0.05)

def char_pos(pos):
    global position
    global row1
    global row2
    position = pos
    if pos == 1:
        if hit and hitpos == 1:
            row1[0] = "X"
        else:
            row1[0] = "0"
        row2[0] = "o"
    elif pos == 2:
        if hit and hitpos == 2:
            row2[0] = "X"
        else:
            row2[0] = "0"
        row1[0] = "o"
    else:
        row1[0]= "o"
        row2[0]= "o"

def msg():
    global row1
    global row2
    global msg1
    global msg2
    msg1 = ""
    msg2 = ""
    for i in row1:
        msg1 += i
    for j in row2:
        msg2 += j

def button_pressed():
    global hit
    global hitpos
    hit = True
    hitpos = position
    hit_delay()
    

def monitor_button():
    btn.when_pressed = button_pressed

def hit_delay():
    time.sleep(0.3)
    global hit
    hit = False

def send():
    global hit
    global hitpos
    print(hit)
    print(hitpos)
    lcd.lcd_message(1,msg1)
    lcd.lcd_message(2,msg2)