#remember to use |p
import requests
import json

bearerToken = "bearer UA22v3mnXq8x6h1l98rX4EPGkN7xr3ZCL1Yzwlopazuv9lx7aHn_JYw1pmfDvj1AoBi_ZoA79Emmv28a-q-7EktODn4QNXj-7HeEEaHKnwMRzUeJkuNvP6Gazm0FJ-6OxX0vgjQH9dRkEr7Ge4QLhvVv4Lnt2ESgEQFZZbMBIj62yJphsFeGPqGbSBD0qoc6YyFpoctNwodl9UkkCIngo5U8rwjGPDt45goDxK_FjnrP8WTYLp963DzsfayvUrRdYEca6xE8fs38a7DBUYunaqV4PuAEIj24SATKeGnrGwf7YWQE3V9USVKStN03F8OUK7hfcw"

baseURL = "https://api.tcgplayer.com/"
productURL = "https://api.tcgplayer.com/catalog/products/"
searchURL = "https://api.tcgplayer.com/catalog/categories/1/search"
searchManifestURL = "https://api.tcgplayer.com/catalog/categories/1/search/manifest"
headers = {"Accept": "application/json", "Authorization": bearerToken}
body = {"limit": 500,"filters": [{"name": "SetName", "values":["New Phyrexia"]}, {"name": "RequiredTypeCb", "values":['Creature']}]}


def printManifestResponse():
	manifestResponse = requests.request("GET", searchManifestURL, headers=headers)
	print(manifestResponse.text)




def main():
	response = requests.request("POST", searchURL, headers=headers, json=body)
	print(response.json())
main()

#""",{"name": "RequiredTypeCb","value": ["Creature"]}"""
