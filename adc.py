#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  adc.py
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
import time


MOSI = 10
MISO = 9
CLK = 11
CS_ = 8
	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN )
GPIO.setup(CLK, GPIO.OUT )
GPIO.setup(CS_, GPIO.OUT )

ADC_val = 0

#Single mode channel 0
SGL = True
ODD = False

#MS_BF
MS_BF = True

GPIO.output(CS_, True)
GPIO.output(CLK, False)
GPIO.output(MOSI, True)


def dec_2_voltage(dec):
	return ((3.3 / 4095) * dec)


def clk_puls():
	GPIO.output(CLK, True)
	#Måske delay her
	GPIO.output(CLK, False)
	#Måske delay her

def read_ADC(channel):
	
	if channel == 0:
		SGL = 1
		ODD = 0
	elif channel == 1:
		SGL = 1
		ODD = 1
			
	#Start udlæsning af ADC value
	GPIO.output(CS_, False)

	#Start puls sendes
	clk_puls()

	#SGL sendes
	GPIO.output(MOSI, SGL)
	clk_puls()

	#ODD sendes 
	GPIO.output(MOSI, ODD)
	clk_puls()

	#MS_BF sendes
	GPIO.output(MOSI, MS_BF)
	clk_puls()
	clk_puls()
	ADC_val = 0
	for i in range(12):
		GPIO.output(CLK, True)
		bit = GPIO.input(MISO)
		#print (bit)
		ADC_val += bit << 11 - i
		GPIO.output(CLK, False)

	#CS høj
	GPIO.output(CS_, True)
	volt = dec_2_voltage(ADC_val)
	return ADC_val, volt


def calc_temp(volt):
	return volt * 100

def calc_lux(volt):
	return volt
	

for i in range(10):
	ADC_val, volt = read_ADC(0)

	print (ADC_val)
	output_str = "{} {}".format(volt, "[V]")
	print (output_str)

	print ("Temperatur : ")
	print('{0:.1f}'.format(calc_temp(volt)))


	ADC_val, volt = read_ADC(1)

	print (ADC_val)
	output_str = "{} {}".format(volt, "[V]")
	print (output_str)

	print ("LUX : ")
	print('{0:.1f}'.format(calc_lux(volt)))
