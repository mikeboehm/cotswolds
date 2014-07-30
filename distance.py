stonehouse = {'lat': 51.746, 'lon': -2.28}
yate = {'lat': 51.5402, 'lon': -2.410989}

north = stonehouse
south = yate

import math
# distance_on_unit_sphere() from: http://www.johndcook.com/python_longitude_latitude.html
def distance_on_unit_sphere(lat1, long1, lat2, long2):

	# Convert latitude and longitude to
	# spherical coordinates in radians.
	degrees_to_radians = math.pi/180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians

	# theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians

	# Compute spherical distance from spherical coordinates.

	# For two locations in spherical coordinates
	# (1, theta, phi) and (1, theta, phi)
	# cosine( arc length ) =
	#	sin phi sin phi' cos(theta-theta') + cos phi cos phi'
	# distance = rho * arc length

	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
		math.cos(phi1)*math.cos(phi2))
	arc = math.acos( cos )

	# Remember to multiply arc by the radius of the earth
	# in your favorite set of units to get length.
	return arc



filename = 'cotswold_way.txt'
file = open(filename)

coords = []
for row in file:
	# Strip \n and then split string into list
	row = row.rstrip().split(',')
	row = {'lat': float(row[0]), 'lon': float(row[1])}
	coords.append(row)

total_distance = 0
previous = False
for point in coords:
	if previous and point['lat'] >= south['lat'] and point['lat'] <= north['lat']:
		total_distance += distance_on_unit_sphere(previous['lat'], previous['lon'], point['lat'], point['lon']) * 6373

	previous = point

print 'Distance is: ' + str(round(total_distance,2)) + ' km'
