





import sys
import time
from machine import I2C, Pin
from time import sleep_ms
from I2C_LCD import I2cLcd

DEFAULT_I2C_ADDR = 0x3F  
import machine
activeBuzzer=Pin(33,Pin.OUT)  
i2c = machine.I2C(1,scl=machine.Pin(14), sda=machine.Pin(13), freq=40000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
ledGREEN=Pin(4, Pin.OUT)             
ledRED=Pin(2, Pin.OUT)


#This imports all of the neccesary modules into the code
#The Pins for the LEDs, the buzzer and the LCD screen are also named






def ringBuzzer():
    for number in range(4):
        activeBuzzer.value(1)
        sleep_ms(500)
        activeBuzzer.value(0)
        sleep_ms(500)

#This tells the buzzer to ring 4 times with 500ms intervals



def completeMessage():
    
    print("done") 
    lcd.clear()
    lcd.putstr("Take your")
    lcd.move_to(0, 1)
    lcd.putstr("tablets")
    ledGREEN.value(1)
    ledRED.value(0)
    ringBuzzer()


#This displays a message on the LCD screen and turns the green LED on while turning the red LED off
#This also calls in the buzzer to ring 4 times    






def readyTimer():    
    if ledRED.value():
        ledRED.value(0)       
    else:
        ledRED.value(1)
        ledGREEN.value(0)
       
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Time Remaining")
    
    button = Pin(12, Pin.IN,Pin.PULL_UP)
   
readyTimer()
  
#This prepares the timer by adding the text "Time Remaining" and turning on the Red LED

#It also tells the code which pin the button is connected to

  
  
  
  
def startTimer(timerLength):
    while timerLength:
    
        hours, remainder = divmod(timerLength, 3600)
        minutes, seconds = divmod(remainder, 60)
    
        lcd.move_to(0, 1)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        lcd.putstr(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
       
        time.sleep(1)
   
        timerLength -=1
    
    if timerLength <= 1:
        completeMessage()
   
   
#This checks the length of the timer found below and converts the hours and minutes to seconds.
        
#The time is printed on the screen with a colon between the hours, minutes and seconds.
        
#The "02d" refers to the distance between the figures
        
#The code then waits 1 second and removes a second
        
#Once the timerLength is less than or equal to 1, the "complete" message is activated.    

while True:
    button = Pin(12, Pin.IN,Pin.PULL_UP)
    if not button.value():
        time.sleep_ms(20)
        if not button.value():  
            print("button pressed!")
            readyTimer()
            startTimer(12*60*60)
            while not button.value():
                time.sleep_ms(20)
    
    
 #This brings in the button and once the button is pressed, it calls in the "readyTimer" and "startTimer" functions
                
 #There is a short sleep after the button is pressed to avoid it being triggered multiple times.   
    
 #The timer length is stated within the argument for "startTimer". This length is 12 hours in seconds   
    