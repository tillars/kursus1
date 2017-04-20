#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mysql.py
#  
#  Copyright 2017 Lars Hansen <lxh@lxh-Aspire-ES1-512>
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
import pymysql

cnx = pymysql.connect(user='root', password='root', host='127.0.0.1', database='for_testing', autocommit=True)            
cur = cnx.cursor()
#cur.execute('INSERT INTO test (name) values ("Tom")')
cur.execute("SELECT * from test")

print(type(cur.description)) 	
print(len(cur.description))
print(cur.description[0])
print(dir(cur))



for row in cur:
	print(row)

cur.close()
cnx.close()                              
           
           
        
                              
    
