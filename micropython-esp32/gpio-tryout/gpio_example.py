from m5stack import lcd
import machine

lcd.print('gpio init start')

pinout = machine.Pin(0, machine.Pin.OUT)
pinout.value(1)

pinin = machine.Pin(2, machine.Pin.IN)
val = pinin.value()


lcd.print('gpio init done.')
