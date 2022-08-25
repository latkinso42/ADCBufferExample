import time
import array
import board
import adcbuffer
import analogio

print('ADC BUFFER')

length = 4
#mybuffer = array.array("B", 0x00 for i in range(length))
mybuffer = array.array("H", 0x0000 for i in range(length))
rate = 500000
adcbuf = adcbuffer.BufferedInput(board.GP27, mybuffer, sample_rate=rate)

z = adcbuf.readmultiple()

adcbuf.deinit()

for k in range(length):
    ss = bin(mybuffer[k])
    print(k, mybuffer[k], ss, ss[0:4], ss[4:8], ss[8:12], ss[12:16])
