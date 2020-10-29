from m5stack import lcd
import machine


lcd.print('dac init start \n')

dac = machine.DAC(machine.Pin(26))
dac.write(128)

lcd.print('dac init done ... \n')
