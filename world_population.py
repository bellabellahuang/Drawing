import json
from pygal.maps.world import World 
from pygal.style import RotateStyle

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

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')