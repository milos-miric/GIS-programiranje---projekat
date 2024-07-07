import pyproj
import numpy as np
from pyproj import Transformer

lat, lon = 45.88404572447533, 18.930809446371192
lat_ca,lon_ca = 45.88404572447533, 18.930809446371192
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca)
xy1 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy1, 'Zoo vrt Kolut')

lat, lon = 46.10017942020357, 19.75277298763358
lat_ca,lon_ca = 46.10017942020357, 19.75277298763358
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca)
xy2 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy2, 'Zoo vrt Palic')

lat, lon = 44.82501963981321, 20.45422560854653
lat_ca,lon_ca = 44.82501963981321, 20.45422560854653
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca)
xy3 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy3, 'Zoo vrt Beograd')

lat, lon = 43.96518551827982, 21.26566265657585
lat_ca,lon_ca = 43.96518551827982, 21.26566265657585
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca)
xy3 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy3, 'Zoo vrt Jagodina')