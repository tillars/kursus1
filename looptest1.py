#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  looptest1.py
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

count = 0
antal = 0

try:
	antal = int(input('Indskriv et tal: '))
except BaseException as e:
	print ('Fejl i tal,',e) 	
	
a = int(input(input('1. niveau: ') + ' (2. niveau): '))	
	

while count < antal:
	print ('Værdi', count)
	count += 1
else:
	print ('Loop end')	
	


nr = [0,1,2,3,4,5,6,7,8,9]

for tal in nr:
	print ('Tal',tal)

print ('Antal',len(nr))

for pos in range(len(nr)):
	try:
		print ('pos=',pos)
		print (nr[pos + 1])
		print('Div fejl',1/0)
	except BaseException as e:
		print ('Fejl',pos)	
		print (e)

