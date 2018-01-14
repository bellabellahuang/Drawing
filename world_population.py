import json
from pygal.maps.world import World 
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
	p_data = json.load(f)

cc_populations = {} # new dictionary
for p in p_data:
	if p['Year'] == '2010':
		country_name = p['Country Name']
		population = int(float(p['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population 

wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')