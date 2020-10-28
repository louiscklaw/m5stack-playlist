from m5stack import lcd
import curl

def test_curl_http():
  if 0 != curl.get('http://www.example.com')[0]:
    print('cannot fetch http example.com')
  else:
    lcd.print('fetch http example.com done')

test_curl_http()
