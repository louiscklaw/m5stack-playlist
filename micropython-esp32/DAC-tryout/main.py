import machine

dac = machine.DAC(machine.Pin(26))
dac.write(128)
