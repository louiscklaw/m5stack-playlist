from m5stack import *
from time import sleep

speaker.volume(2)
speaker.tone(freq=1800)
speaker.tone(freq=1800, duration=200) # Non-blocking

for freq_i in range(2000,20000, 100):
  sleep(1)
  speaker.volume(2)
  speaker.tone(freq=freq_i)
  speaker.tone(freq=freq_i, duration=200) # Non-blocking
