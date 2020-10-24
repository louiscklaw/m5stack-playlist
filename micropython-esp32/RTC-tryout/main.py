import machine
import utime

rtc = machine.RTC()
rtc.ntp_sync(server="hr.pool.ntp.org", tz="CET-1CEST")
rtc.synced()
True
utime.gmtime()
(2018, 1, 29, 16, 3, 18, 2, 29)
utime.localtime()
(2018, 1, 29, 17, 3, 30, 2, 29)
