import RPi.GPIO as GPIO

cs = 8
clk = 11
din = 10
dout = 9


def init_adc():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	#set retning in/out
	GPIO.setup(cs, GPIO.OUT)
	GPIO.setup(clk, GPIO.OUT)
	GPIO.setup(din, GPIO.OUT)
	GPIO.setup(dout, GPIO.IN)
    
    #set start niveau
	GPIO.output(cs, True)
	GPIO.output(clk, False)
	GPIO.output(din, True)
    
    
def clk_puls():
	#GPIO.output(clk, False)
	GPIO.output(clk, True)
	GPIO.output(clk, False)
	    
    
def read_adc(channel):
	adc_val = 0
	GPIO.output(cs, False)
	GPIO.output(din, True)
	
	#startbit
	clk_puls()
	
	#SGL
	clk_puls()
	
	odd = True
	if channel == 0:
		odd = False
	else:	
		odd = True
		
	GPIO.output(din, odd)
	
	#odd
	clk_puls()
		
	#ms
	GPIO.output(din, False)	
	clk_puls()	
		
		
	#udlaes vaerdi fra adc
	
	for bit in range(13):
		clk_puls()
		adc_val <<= 1
		if (GPIO.input(dout)):
			adc_val |= 0x1
	
	GPIO.output(cs, True)
	adc_val >>= 1
	return adc_val
    
    
    
#Main     
init_adc()
        
channel = 0    
res = read_adc(channel)
print(str(res))

volt = 3.3 / 4095 * res
print(str(volt) + " V")

channel = 1    
res = read_adc(channel)
print(str(res))

volt = 3.3 / 4095 * res
print(str(volt) + " V")
