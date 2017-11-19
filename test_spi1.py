#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_spi1.py
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
import subprocess

       
def ctrlCHandler(*whatever):
    # Just sets the value of CONTROL_C
    global CONTROL_C
    CONTROL_C = True

                 
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
	for i in range(13):
		GPIO.output(clockpin, True )
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1


	GPIO.output(cspin, True)        
	adcout >>= 1 # first bit is 'null' so drop it
	return adcout




#Main
CONTROL_C = False
print (" ")
print ("CTRL-C to exit")
print (" ")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
subprocess.call('setterm -cursor off', shell=True)

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
adc_channel0 = 0;
pos = 0
temp_avg = []

while True:
	trim_pot = readadc(adc_channel0, SPICLK, SPIMOSI, SPIMISO, SPICS)
	voltage = 3.3 * trim_pot / 4096 
	temp = voltage * 100
	temp_avg.append(temp)
	print ("Digital:", trim_pot , " Voltage:", round(voltage, 3), " Temp:", round(temp, 1), "avg:")
	
	time.sleep(0.0001)
	pos += 1
	if pos == 30:		
		pos = 0	
		del temp_avg
		temp_avg = []
	time.sleep(0.1)

if CONTROL_C: sys.exit(0)
