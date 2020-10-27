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
    lcd.print("WiFi started")
    utime.sleep_ms(500)

    rtc = machine.RTC()
    lcd.print("Synchronize time from NTP server ...")
    rtc.ntp_sync(server="hr.pool.ntp.org")
    tmo = 100
    while not rtc.synced():
        utime.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break

    if tmo > 0:
        lcd.print("Time set")
        utime.sleep_ms(500)
        t = rtc.now()
        utime.strftime("%c")
        lcd.print("")

def helloworld_wifi():
  lcd.print('helloworld wifi')