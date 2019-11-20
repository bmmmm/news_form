import geonamescache
gc = geonamescache.GeonamesCache()

all_cities_low = gc.get_cities()
all_countries_low = gc.get_countries()

for city in all_cities_low.values():
	#{'geonameid': 895061, 'name': 'Bindura', 
	#'latitude': -17.30192, 'longitude': 31.33056, 'countrycode': 'ZW', 
	#'population': 37423, 'timezone': 'Africa/Harare', 'admin1code': '03'}
	#print(city['name'].lower(), city['countrycode'])
	pass

for country in all_countries_low.values():
	#{'geonameid': 8505032, 'name': 'Netherlands Antilles', 'iso': 'AN', 'iso3': 'ANT', 
	#'isonumeric': 530, 'fips': 'NT', 'continentcode': 'NA', 'capital': 'Willemstad', 
	#'areakm2': 960, 'population': 300000, 'tld': '.an', 'currencycode': 'ANG', 
	#'currencyname': 'Guilder', 'phone': '599', 'postalcoderegex': '', 
	#'languages': 'nl-AN,en,es', 'neighbours': 'GP'}
	#print(country)
	pass