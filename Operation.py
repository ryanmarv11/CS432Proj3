import requests
import json

bearerToken = "bearer UA22v3mnXq8x6h1l98rX4EPGkN7xr3ZCL1Yzwlopazuv9lx7aHn_JYw1pmfDvj1AoBi_ZoA79Emmv28a-q-7EktODn4QNXj-7HeEEaHKnwMRzUeJkuNvP6Gazm0FJ-6OxX0vgjQH9dRkEr7Ge4QLhvVv4Lnt2ESgEQFZZbMBIj62yJphsFeGPqGbSBD0qoc6YyFpoctNwodl9UkkCIngo5U8rwjGPDt45goDxK_FjnrP8WTYLp963DzsfayvUrRdYEca6xE8fs38a7DBUYunaqV4PuAEIj24SATKeGnrGwf7YWQE3V9USVKStN03F8OUK7hfcw"
headers = {"Accept": "application/json", "Authorization": bearerToken}
baseURL = "https://api.tcgplayer.com/"
mode = "None"
expansion = "None"
setDict = {}


class Card:
	def __init__(self, productId, power, toughness, cmc):
		self.productId = productId
		self.power = power
		self.toughness = toughness
		self.cmc = cmc
		print(expansion)
		self.date = getDate(expansion)
		self.skuList = []
		self.priceList = []
		self.avgPrice = 0.0
		self.priceScore = 0.0
		self.baseScore = (self.power + self.toughness) / self.cmc

	def setSKUList(self):
		skuURL = baseURL + "catalog/products/" + str(self.productId) + "/skus"
		response = requests.request("GET", skuURL, headers=headers)
		responseJSON = response.json()
		results = responseJSON['results']
		results = results[:8]
		for item in results:
			self.skuList.append(item['skuId'])

	def setPriceList(self):
		priceURL = baseURL + "pricing/sku/"
		for sku in self.skuList:
			response = requests.request("GET", priceURL + str(sku), headers=headers)
			responseJSON = response.json()
			if responseJSON['results'][0]['marketPrice'] != None:
				self.priceList.append(responseJSON['results'][0]['marketPrice'])
		self.avgPrice = sum(self.priceList) / len(self.priceList)

	def getDuelScore(self):
		if self.date >= 2007 and self.date <= 2010:
			return self.getPriceScore(1.2)
		elif self.date >= 2011 and self.date <= 2014:
			return self.getPriceScore(1.07)
		elif self.date >= 2015 and self.date <= 2018:
			return self.getPriceScore(1.03)
		else:
			print("Invalid date for DuelDecks.")

	def getPioneerScore(self):
		if self.date >= 2012 and self.date <= 2014:
			return self.getPriceScore(1.15)
		elif self.date >= 2015 and self.date <= 2021:
			return self.getPriceScore(1.09)
		else:
			print("Invalid date for Pioneer.")

	def getModernScore(self):
		if self.date >= 2003 and self.date <= 2014:
			return self.getPriceScore(1.3)
		elif self.date >= 2015 and self.date <= 2021:
			return self.getPriceScore(1.02)
		else:
			print("Invalid date for Modern.")

	def getPreModernScore(self):
		if self.date >= 1994 and self.date <= 1999:
			return self.getPriceScore(1.1)
		elif self.date >= 2000 and self.date <= 2003:
			return self.getPriceScore(1.07)
		else:
			print("Invalid date for PreModern")

	def getPriceScore(self, dateConstant):
		return dateConstant + (.5 * ((10 / self.avgPrice) / 20))

	def setPriceScore(self, mode):
		if mode == "Duel":
			self.priceScore = self.getDuelScore()
		elif mode == "Pioneer":
			self.priceScore = self.getPioneerScore()
		elif mode == "Modern":
			self.priceScore = self.getModernScore()
		elif mode == "PreModern":
			self.priceScore = self.getPreModernScore()
		else:
			print("Error, invalid mode.")
	def toString(self):
		return "productId: " + str(self.productId) + " power: " + str(self.power) + " toughness: " + str(self.toughness) + " cmc: " + str(self.cmc)



def setSetDict():
	setDict["Fourth Edition"] = 1995
	setDict["Ice Age"] = 1995
	setDict["Homelands"] = 1995

	setDict["Mirage"] = 1996
	setDict["Alliances"] = 1996

	setDict["Weatherlight"] = 1997
	setDict["Tempest"] = 1997
	setDict["Fifth Edition"] = 1997
	setDict["Visions"] = 1997

	setDict["Urza's Saga"] = 1998
	setDict["Exodus"] = 1998
	setDict["Stronghold"] = 1998


	setDict["Mercadian Masques"] = 1999
	setDict["Urza's Destiny"] = 1999
	setDict["Classic Sixth Edition"] = 1999
	setDict["Urza's Legacy"] = 1999

	setDict["Invasion"] = 2000
	setDict["Prophecy"] = 2000
	setDict["Nemesis"] = 2000

	setDict["Odyssey"] = 2001
	setDict["Apocalypse"] = 2001
	setDict["Core Set Seventh Edition"] = 2001
	setDict["Planeshift"] = 2001

	setDict["Onslaught"] = 2002
	setDict["Torment"] = 2002
	setDict["Judgment"] = 2002

	setDict["Mirrodin"] = 2003
	setDict["Core Set Eighth Edition"] = 2003
	setDict["Scourge"] = 2003
	setDict["Legions"] = 2003

	setDict["Champions of Kamigawa"] = 2004
	setDict["Fifth Dawn"] = 2004
	setDict["Darksteel"] = 2004

	setDict["Ravnica: City of Guilds"] = 2005
	setDict["Core Set Ninth Edition"] = 2005
	setDict["Saviors of Kamigawa"] = 2005
	setDict["Betrayers of Kamigawa"] = 2005

	setDict["Time Spiral"] = 2006
	setDict["Dissension"] = 2006
	setDict["Coldsnap"] = 2006
	setDict["Guildpact"] = 2006

	setDict["Lorwyn"] = 2007
	setDict["Core Set Tenth Edition"] = 2007
	setDict["Future Sight"] = 2007
	setDict["Planar Chaos"] = 2007

	setDict["Shards of Alara"] = 2008
	setDict["Eventide"] = 2008
	setDict["Shadowmoor"] = 2008
	setDict["Morningtide"] = 2008

	setDict["Zendikar"] = 2009
	setDict["2010 Core Set"] = 2009
	setDict["Alara Reborn"] = 2009
	setDict["Conflux"] = 2009

	setDict["Scars of Mirrodin"] = 2010
	setDict["2011 Core Set"] = 2010
	setDict["Rise of the Eldrazi"] = 2010
	setDict["Worldwake"] = 2010

	setDict["Innistrad"] = 2011
	setDict["2012 Core Set"] = 2011
	setDict["New Phyrexia"] = 2011
	setDict["Mirrodin Besieged"] = 2011

	setDict["Return to Ravnica"] = 2012
	setDict["2013 Core Set"] = 2012
	setDict["Avacyn Restored"] = 2012
	setDict["Dark Ascension"] = 2012

	setDict["Theros"] = 2013
	setDict["2014 Core Set"] = 2013
	setDict["Gatecrash"] = 2013
	setDict["Dragon's Maze"] = 2013

	setDict["Khans of Tarkir"] = 2014
	setDict["2015 Core Set"] = 2014
	setDict["Journey Into Nyx"] = 2014
	setDict["Born of the Gods"] = 2014

	setDict["Battle for Zendikar"] = 2015
	setDict["Magic Origins"] = 2015
	setDict["Dragons of Tarkir"] = 2015
	setDict["Fate Reforged"] = 2015

	setDict["Kaladesh"] = 2016
	setDict["Eldritch Moon"] = 2016
	setDict["Shadows over Innistrad"] = 2016
	setDict["Oath of the Gatewatch"] = 2016

	setDict["Ixalan"] = 2017
	setDict["Amonkhet"] = 2017
	setDict["Aether Revolt"] = 2017
	setDict["Hour of Devastation"] = 2017

	setDict["Guilds of Ravnica"] = 2018
	setDict["Core Set 2019"] = 2018
	setDict["Dominaria"] = 2018
	setDict["Rivals of Ixalan"] = 2018

	setDict["Throne of Eldraine"] = 2019
	setDict["Core 2020"] = 2019
	setDict["Ravnica Allegiance"] = 2019
	setDict["War of the Spark"] = 2019

	setDict["Zendikar Rising"] = 2020
	setDict["Core Set 2021"] = 2020
	setDict["Ikoria: Lair of Behemoths"] = 2020
	setDict["Theros BeyondDeath"] = 2020

	setDict["Innistrad: Crimson Vow"] = 2021
	setDict["Innistrad: Midnight Hunt"] = 2021
	setDict["Adventures in the Forgotten Realms"] = 2021
	setDict["Strixhaven: School of Mages"] = 2021
	setDict["Kaldheim"] = 2021

	setDict["Modern Horizons"] = 2019
	setDict["Modern Horizons 2"] = 2021

def getDate(setName):
	return setDict[setName]


def main():
	b = Card(39610, 2, 2, 2)
	b.setSKUList()
	b.setPriceList()
	print(mode)
	b.setPriceScore(mode)
	f = open('Modern/NPH.json')
	data = json.load(f)
	cardList = []
	for item in data['data']['cards']:
		if 'Creature' in item['types']:
			if item['power'] != '*':
				power = int(item['power'])
			else:
				power = 2
			if item['toughness'] != '*':
				toughness = int(item['toughness'])
			else:
				toughness = 2
			cmc = float(item['convertedManaCost'])
			cardList.append(Card(2, power, toughness, cmc))
	for card in cardList:
		print(card.toString())
			

mode = "Modern"
expansion = "New Phyrexia"
setSetDict()
main()







