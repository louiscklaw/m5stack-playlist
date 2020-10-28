import machine

p1 = machine.Pin(27)
p1.init(p1.OUT)
p1.value(1)

def tcb(timer):
  print('tcb triggered')

t1 = machine.Timer(2)
t1.init(period=1000, mode=t1.PERIODIC, callback=tcb)
