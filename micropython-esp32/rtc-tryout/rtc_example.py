import machine
import utime
from time import sleep
from m5stack import lcd

rtc = machine.RTC()
rtc.ntp_sync(server="stdtime.gov.hk", tz="HKT-8")
rtc.synced()

while True:
  lcd.clear()

  hk_time = utime.localtime()
  year = hk_time[0]
  month = hk_time[1]
  day = hk_time[2]
  hour= hk_time[3]
  minute = hk_time[4]
  second = hk_time[5]


  lcd.print(year, 0,0)
  lcd.print(month, 40*1,0)
  lcd.print(day, 40*2,0)
  lcd.print(hour, 40*3,0)
  lcd.print(minute, 40*4,0)
  lcd.print(second, 40*5,0)


  sleep(1)
