import pyfirmata

comport='COM5'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:8:o')

def led(total):
    if total==0:
        led_1.write(0)
    elif total==1:
        led_1.write(1)
