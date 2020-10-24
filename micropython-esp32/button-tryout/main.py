from m5stack import lcd

lcd.print('hello world!\n')

from m5stack import *

def on_wasPressed():
  lcd.print('Button B was Pressed\n')

def on_wasReleased():
  lcd.print('Button B was Released\n')

def on_releasedFor():
  lcd.print('Button B released for 1.2s press hold\n')

buttonB.wasPressed(on_wasPressed)
buttonB.wasReleased(on_wasReleased)
buttonB.releasedFor(1.2, on_releasedFor)
