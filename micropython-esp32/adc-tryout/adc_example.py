from m5stack import lcd
import machine

lcd.print('adc start')

adc = machine.ADC(35)
adc.read()

lcd.print('adc init done')
