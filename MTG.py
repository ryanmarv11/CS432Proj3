import json

f = open('PUMA.json')

data = json.load(f)

for i in data['data']['cards']:
	if 'modern' in i['legalities']:
		if i['legalities']['modern'] == 'Legal' and i['types'] == ['Creature']:
			print(i.values())
			break

	
