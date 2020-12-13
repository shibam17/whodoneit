#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from twilio.rest import Client
from twilio import twiml
import os

ACCOUNT_SID=# account sid here
AUTH_TOKEN=#auth token here

client = Client(ACCOUNT_SID,AUTH_TOKEN)
FROM = #twilio number
TO =#particpant mobile number
clues ={1:"On my way back to my hideout.I saw this guy.This guy has 4 legs and has hair at night?You might have seen him this morning.Probably I've left my next clue under it"
,2:"Wah!so you do have detective skills. but probably that won't help you get me.This thing is white in color but turns yellow when falls on the floor.Probably you'll see something here"
,3:"Haa! good thinking there...but I guess you'll have to try harder to reach me.Meet one of my loyal servants.He loses his head in the morning and get it back at nights.You think you can find him? Let's see"
,4:"hmm good thinking there..I under estimated you..haha now see if you can guess this...'I stand up and make your day brighter'"
,5:"I'm used on heads,toes maybe your entire body,the more I work for my boss the thinner I grow"
,6:"You've come this far...I appreciate that...But here on things will not be the same..let's not meet again...still I'll give you a chance. 'this guy likes amplifying what is fed into him and he speaks loudly cuz he's probably the best in it'"
,7:"Wow you just solved one of the hardes one! lemme give u an easy one : think you can find me where you find books..let's see"
,8:"haha...this is probably the funniest place to find a clue 'one sheet,two sheets,three sheets, some use more some less'"
,9:"You've almost found your way...let us see if you break the supreme ones mystery:- 'time to think time to chill,for your next due please go here for a cool cool drink'"
,10:"you fool! you started searching for me from the place where i am still hiding..haha"}

codes=[4521,3895,1235,7854,1256,9561,3644,4932,1099,1007]

level=1
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
 
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
 
  # Initialise display
  lcd_init()
  lcd_string("  Sherlock Home  ",LCD_LINE_1)
  lcd_string("Who Doneit Hacks",LCD_LINE_2)
  time.sleep(15)
  lcd_string("First Clue sent",LCD_LINE_1)
  lcd_string("",LCD_LINE_2)
  send_clue(clues[1])
  while True:
 
    # Send some test
    global level
    lcd_string("Enter Clue Code",LCD_LINE_1)
    lcd_string("",LCD_LINE_2)
    print('Enter clue code')
    n=int(input()) # 3 second delay
    if n==codes[level]:
        lcd_string("Yaaay you found it",LCD_LINE_1)
        level+=1
        send_clue(clues[level])
        time.sleep(3)
    elif n==1077 and level==10:
        lcd_string("You found Him",LCD_LINE_1)
        lcd_string("Congrats! You won",LCD_LINE_2)
        time.sleep(3)
        lcd_string("GAME OVER",LCD_LINE_1)
        lcd_string("",LCD_LINE_2)
        exit()
    else:
        lcd_string("Wrong Anwer",LCD_LINE_1)
        lcd_string("Try harder",LCD_LINE_2)
        time.sleep(3)
    # Send some text

     # 3 second delay
    
    

def send_clue(clue):
    body=clue
    client.messages \
                .create(
                    body=body,
                    from_=FROM, #use your twilio no here
                    to=TO, #use your verified phone no. here
                    )
    lcd_string("Next clue sent",LCD_LINE_1)
    
def lcd_init():
  lcd_display(0x28,LCD_CMD) # Selecting 4 - bit mode with two rows
  lcd_display(0x0C,LCD_CMD) # Display On,Cursor Off, Blink Off
  lcd_display(0x01,LCD_CMD) # Clear display

  time.sleep(E_DELAY)
 
def lcd_display(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_display(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_display(ord(message[i]),LCD_CHR)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_display(0x01, LCD_CMD)
    GPIO.cleanup()
