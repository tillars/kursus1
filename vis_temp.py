#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filetest.py
#  
#  Copyright 2017 LXH <LXH@LXH-CND4161DRK>
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
#!/usr/bin/python3
import sys


#file name
file_name = "index.html"


#file contents
file_text = """
<!DOCTYPE html>
<html>
    <META HTTP-EQUIV="refresh" CONTENT="10">
    <body>
        <font color="black">
            <h1>Temperatur: </h1>
        </font>
        <font color="blue">  
            <p>Temp =< 28 °C</p>
        </font>
        <font color="red">  
            <p>Temp > 28 °C</p>
        </font>
    </body>
</html>
"""


#open file stream
try:
    file = open(file_name, "w")
except IOError:
    print ("There was an error writing to"), file_name
    sys.exit()
    

#write text to file
file.write(file_text)
file.write("\n")
file.close()


#print file text
print(file_text)

