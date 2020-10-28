from m5stack import lcd

import gc

lcd.print('checking RAM space')
lcd.print('\n')

lcd.print(gc.mem_free() / 8)
lcd.print('\n')