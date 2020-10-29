from m5stack import lcd
import machine

lcd.print('pwm init start\n')

pwm = machine.PWM(26)
pwm.freq(5000)
pwm.duty(66) # 0.0 ~ 100.0

lcd.print('pwm init done\n')
