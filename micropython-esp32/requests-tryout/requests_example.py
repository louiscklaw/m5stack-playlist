import requests
from m5stack import lcd

r = requests.get('http://www.example.com')

def test_requests_http_example():
  r = requests.get('http://www.example.com')

  if (r[0] != 200):
    lcd.print('error found during fetching www.example.com with requests lib\n')
  else:
    lcd.print('test request to www.example.com done\n')

test_requests_http_example()
