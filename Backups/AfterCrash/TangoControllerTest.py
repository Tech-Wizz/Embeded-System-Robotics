import serial, sys, time

from TangoController import Tango_Controller

usb = serial.Serial('/dev/ttyACM0')

tangoControl = Tango_Controller(usb)
target = 4200

tangoControl.forward(2)
time.sleep(2)
tangoControl.stop()
time.sleep(1.5)
tangoControl.backward(2)
time.sleep(1.5)
tangoControl.stop()
tangoControl.spin_left(2)
time.sleep(1.5)
tangoControl.stop()
tangoControl.spin_right(2)
time.sleep(1.5)
tangoControl.stop()
