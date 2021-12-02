import json

f = open('Modern/NPH.json')

data = json.load(f)

for i in data['data']['cards']:
	if 'modern' in i['legalities']:
		if i['legalities']['modern'] == 'Legal' and i['types'] == ['Creature']:
			print(i['identifiers']['tcgplayerProductId'])

	
