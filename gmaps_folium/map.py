# import folium package
import folium

my_map4 = folium.Map(location = [28.5011226, 77.4099794],
										zoom_start = 12)

folium.Marker([28.704059, 77.102490],
			popup = 'Your Location').add_to(my_map4)

folium.Marker([28.5011226, 77.4099794],
			popup = 'Pet Location').add_to(my_map4)

# Add a line to the map by using line method .
# it connect both coordinates by the line
# line_opacity implies intensity of the line

folium.PolyLine(locations = [(28.704059, 77.102490), (28.5011226, 77.4099794)],
				line_opacity = 0.5).add_to(my_map4)

my_map4.save("my_map4.html")
