#Name: Christopher Mena
#Email: christopher.mena66@myhunter.cuny.edu
#Date: November 13, 2019
#Creates a html map of NY centered at the given coordinates and popup at Hunter College

#import folium
import folium

#Create a map, centered 40.75, -74.125, and zoomed out a bit:
mapCUNY = folium.Map(location=[40.75, -74.125],zoom_start=11)

#Place a market at location with popup "Hunter College"
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile='nycMap.html')