from m5stack import lcd

import ubinascii
import os

lcd.print('checking ROM space')
lcd.print('\n')

statvfs_fields = ['bsize','frsize','blocks','bfree','bavail','files','ffree',]
info = dict(zip(statvfs_fields, os.statvfs('/flash')))

lcd.print(info)
lcd.print('\n')
lcd.print(info['bsize'] * info['bfree'] / 8 / 1024)
lcd.print('\n')

lcd.print('check rom done ...')
lcd.print('\n')