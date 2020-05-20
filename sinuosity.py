import sys
import fiona
from shapely.geometry import LineString

filename = sys.argv[1]

with fiona.open(filename) as shp:
    start_pt = shp[0]['geometry']['coordinates'][0]
    end_pt = shp[0]['geometry']['coordinates'][-1]
    straight_line = LineString((start_pt, end_pt))
    line = LineString(shp[0]['geometry']['coordinates'])

sinuosity = line.length / straight_line.length

print(sinuosity)
