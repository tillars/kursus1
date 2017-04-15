#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test1.py
#  
#  Copyright 2017  <pi@raspberrypi>
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
#
#HUSK VIRKER KUN MED python2.7!!!!!!!!!
import wiringpi
import time
from datetime import datetime


print ('*************')
a = 10

print (a)
print (id(a))

b = a

print (b)
print (id(b))

b = 12
a = 13

print (a)
print (id(a))
print (b)
print (id(b))
print ('*************')

print (2+2)
print ("Hello World")

print (dir(time))
print ("Sleep")
print (dir(time.sleep))
print (time.gmtime())

print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print (datetime.now().strftime('%S'))

print (wiringpi.piBoardRev())


wiringpi.wiringPiSetup()

#pinMode pin, in/out (0=in 1=out)
wiringpi.pinMode(0, 1)

loop = 0
while (loop < 20):
    wiringpi.digitalWrite(0, 0)
    time.sleep(2)
    wiringpi.digitalWrite(0, 1)
    time.sleep(2)
    loop = loop + 1
    print (loop)
    



