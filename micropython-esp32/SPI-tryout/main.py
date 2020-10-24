from machine import SPI, Pin

spi = SPI(
    spihost=SPI.HSPI,
    baudrate=2600000
    sck=Pin(18),
    mosi=Pin(23),
    miso=Pin(19),
    cs=Pin(4)
)

spi.write(buf) #NOHEAP
spi.read(nbytes, *, write=0x00) #write is the byte to ?output on MOSI for each byte read in
spi.readinto(buf, *, write=0x00) #NOHEAP
spi.write_readinto(write_buf, read_buf) #NOHEAP; write_buf and read_buf can be the same
