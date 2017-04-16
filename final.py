#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  final.py
#  
#  Copyright 2017 root <root@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import time
import os
import sys
import RPi.GPIO as GPIO
from decimal import *

                 
# read SPI data from MCP3208 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1

        
	GPIO.output(cspin   , True)
	GPIO.output(clockpin, False)  # start clock low
	GPIO.output(cspin   , False)  # bring CS low
	commandout = adcnum
	commandout |= 0x18            # start bit + single-ended bit
	commandout <<= 3              # we only need to send 5 bits here


	for i in range(4):
		if (commandout & 0x80):
			GPIO.output(mosipin, True )
		else:
			GPIO.output(mosipin, False)
            
		commandout <<= 1
		GPIO.output(clockpin, True )
		GPIO.output(clockpin, False)


	adcout = 0
	# read in one empty bit, one null bit and 12 ADC bits
	# pro desetibitovy prevodnik tu bylo puvodne cislo 12
	for i in range(13):
		GPIO.output(clockpin, True )
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1


	GPIO.output(cspin, True)        
	adcout >>= 1 # first bit is 'null' so drop it
	return adcout


def get_temp():
	adc_channel0 = 0;
	temp_avg = []
	trim_pot = readadc(adc_channel0, SPICLK, SPIMOSI, SPIMISO, SPICS)
	voltage = 3.3 * trim_pot / 4096 
	return voltage * 100

#	temp_avg.append(temp)
#	print ("Digital:", trim_pot , " Voltage:", round(voltage, 3), " Temp:", round(temp, 1), "avg:")
	
#	time.sleep(0.0001)
#	pos += 1
#	if pos == 30:		
#		pos = 0	
#		del temp_avg
#		temp_avg = []
#	time.sleep(0.1)


#main
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# change these as desired - they're the pins connected from the SPI port on the ADC to the RPi
SPICLK  = 11
SPIMISO = 9
SPIMOSI = 10
SPICS   = 8
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN )
GPIO.setup(SPICLK,  GPIO.OUT)
GPIO.setup(SPICS,   GPIO.OUT)


#file name
file_name = "index.html"

while 1:
	#file contents
	file_text = """<!DOCTYPE html>
	<html>
		<META HTTP-EQUIV="refresh" CONTENT="1">
		<body>
			<font color="black">
				<h1>Temperatur: </h1>
			</font>
			<font color="#color#">  
				<p>Temp = #temp# &#x2103;</p>
			</font>
		</body>
	</html>"""
	
	
	#temp value
	temperatur = get_temp()
	temp = str('{0:.2f}'.format(temperatur))
	#temp color - blue/red
	if float(temp) > 24:
		temp_color = "red"
	else:
		temp_color = "blue"
    

	#replace in html contents
	file_text = file_text.replace('\n','')
	file_text = file_text.replace('#color#',temp_color)
	file_text = file_text.replace('#temp#',temp)


	#open file stream
	try:
		file = open(file_name, "w")
	except IOError:
		print ("There was an error writing to"), file_name
		sys.exit()
    

	#write text to file
	file.write(str(file_text))
	file.write("\n")
	file.close()
	#print file text
	print('{0:.2f}'.format(temperatur))
	time.sleep(1)
	
