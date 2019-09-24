import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#Mendefinisikan pin output motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#Mendefinisikan pin input remote
GPIO.setup(2, GPIO.IN)# tombol maju
GPIO.setup(3, GPIO.IN)# tombol kiri
GPIO.setup(17, GPIO.IN)# tombol kanan
GPIO.setup(27, GPIO.IN)# tombol mundur

while True:
    i=GPIO.input(2)
    j=GPIO.input(3)
    k=GPIO.input(17)
    l=GPIO.input(27)
    # Kondisi 1 = tombol ditekan, dan 0 = tombol dilepas
    if i==1:
        GPIO.output(14,0)  
        GPIO.output(15,1) 
        GPIO.output(23,0) 
        GPIO.output(24,1)
        print('MAJU')
        
    elif j==1:
        GPIO.output(14,1) 
        GPIO.output(15,0)
        GPIO.output(23,0)  
        GPIO.output(24,1)
        print('BELOK KIRI')
        
    elif k==1:
        GPIO.output(14,0)  
        GPIO.output(15,1)  
        GPIO.output(23,1) 
        GPIO.output(24,0)
        print('BELOK KANAN')
        
    elif l==1:
        GPIO.output(14,1)  
        GPIO.output(15,0)  
        GPIO.output(23,1) 
        GPIO.output(24,0)
        print('MUNDUR')
        
    else:
        GPIO.output(14,0)  
        GPIO.output(15,0)  
        GPIO.output(23,0)  
        GPIO.output(24,0)
        print('DIAM')
