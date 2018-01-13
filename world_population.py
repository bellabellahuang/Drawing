import json

from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
	p_data = json.load(f)

for p in p_data:
	if p['Year'] == '2010':
		country_name = p['Country Name']
		population = int(float(p['Value']))
		code = get_country_code(country_name)
		if code:
			print(code + ": " + str(population))
		else:
			print('ERROR - ' + country_name)