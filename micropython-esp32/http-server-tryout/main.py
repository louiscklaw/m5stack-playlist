from m5stack import lcd
lcd.print('hello world!\n')

import machine, network, utime


lcd.print("")
lcd.print("Starting WiFi ...")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("logic_debug",'ohzei7eexaimo3Ae')
tmo = 50
while not sta_if.isconnected():
    lcd.print('retrying connect \n')
    utime.sleep_ms(1000)
    tmo -= 1
    if tmo == 0:
        sta_if.disconnect()
        break

if tmo > 0:
    lcd.print("WiFi started")
    utime.sleep_ms(500)
    lcd.print(sta_if.ifconfig())

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
        lcd.print(utime.strftime("%c"))
        lcd.print('\n')



from    microWebSrv import MicroWebSrv
import _thread

def _httpHandlerTestGet(httpClient, httpResponse) :
	content = """\
	<!DOCTYPE html>
	<html lang=fr>
        <head>
        	<meta charset="UTF-8" />
            <title>TEST GET</title>
        </head>
        <body>
            <h1>TEST GET</h1>
            Client IP address = %s
            <br />
			<form action="/TEST" method="post" accept-charset="ISO-8859-1">
				First name: <input type="text" name="firstname"><br />
				Last name: <input type="text" name="lastname"><br />
				<input type="submit" value="Submit">
			</form>
        </body>
    </html>
	""" % httpClient.GetIPAddr()
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

def _httpHandlerTestPost(httpClient, httpResponse) :
	formData  = httpClient.ReadRequestPostedFormData()
	firstname = formData["firstname"]
	lastname  = formData["lastname"]
	escape    = httpClient.GetServer().HTMLEscape
	content   = """\
	<!DOCTYPE html>
	<html lang=fr>
		<head>
			<meta charset="UTF-8" />
            <title>TEST POST</title>
        </head>
        <body>
            <h1>TEST POST</h1>
            Firstname = %s<br />
            Lastname = %s<br />
        </body>
    </html>
	""" % (escape(firstname), escape(lastname))
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

routeHandlers = [
	( "/test",	"GET",	_httpHandlerTestGet ),
	( "/test",	"POST",	_httpHandlerTestPost )
]

srv = MicroWebSrv(routeHandlers=routeHandlers)

srv.Start(threaded=True)
