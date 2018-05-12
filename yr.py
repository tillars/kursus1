#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request


def get_data(url = 'http://www.yr.no/place/Denmark/Zealand/Roskilde_Airport/forecast_hour_by_hour.xml'):
    url = 'http://www.yr.no/place/Denmark/Zealand/Roskilde_Airport/forecast_hour_by_hour.xml'
    #url = 'http://www.yr.no/place/Denmark/Midtjylland/%C3%85rhus_Sygehus_Skejby/forecast_hour_by_hour.xml'

    with urllib.request.urlopen(url) as response:
        xml_ = response.read()

    return xml_.decode("utf-8")

with open("/home/vejr.xml", "w") as file:
    file.write(get_data())

print ("End")

