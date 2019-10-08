#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  adc1.py
#  
#  Copyright 2018  <pi@raspberrypi>
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
import RPi.GPIO as GPIO

#fra adc
cs = 8
clk = 11
din = 10
dout = 9




def initprogram():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	#sætter retning
	GPIO.setup(cs, GPIO.OUT)
	GPIO.setup(clk, GPIO.OUT)
	GPIO.setup(din, GPIO.OUT)
	GPIO.setup(dout, GPIO.IN)

	#sætter niveau
	GPIO.output(cs, True)
	GPIO.output(clk, False)
	GPIO.output(din, True)


	

def read_adc(channel):
	pass
	
	

	
#main
initprogram()

GPIO.output(cs, False)

#start
GPIO.output(clk, True)
GPIO.output(clk, False)

#@channel 0 -> command 101

#sgl
GPIO.output(din, True)
GPIO.output(clk, True)
GPIO.output(clk, False)

#odd
GPIO.output(din, False)
GPIO.output(clk, True)
GPIO.output(clk, False)

#ms
GPIO.output(din, False)
GPIO.output(clk, True)
GPIO.output(clk, False)

#udlæs data - værdi fra adc

adc = 0

for i in range(13):
	GPIO.output(clk, True)
	GPIO.output(clk, False)
	adc <<= 1
	if (GPIO.input(dout)):
		adc |= 0x1


GPIO.output(cs, True)        
adc >>= 1
print(adc)

volt = (adc/4095)*3.3

print(volt)
