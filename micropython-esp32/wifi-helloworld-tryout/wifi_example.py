from m5stack import lcd
import machine, network, utime

lcd.print("")
lcd.print("Starting WiFi ...")

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("logic_debug",'ohzei7eexaimo3Ae')
tmo = 50
while not sta_if.isconnected():
  utime.sleep_ms(100)
  tmo -= 1
  if tmo == 0:
    sta_if.disconnect()
    break

if tmo > 0:
  utime.sleep_ms(500)
  lcd.print('IP address : ')
  lcd.print(sta_if.ifconfig()[0])
  lcd.print('\n')

  lcd.print("WiFi started")
  lcd.print('\n')

def helloworld_wifi():
  lcd.print('helloworld wifi')