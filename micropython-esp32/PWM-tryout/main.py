import machine
pwm = machine.PWM(26)
pwm.freq(5000)
pwm.duty(66) # 0.0 ~ 100.0
