import requests, json, re, random
from bs4 import BeautifulSoup
from cleantext import clean
from urllib.parse import quote
from pathvalidate import sanitize_filepath
from PIL import Image

groupName = "GROUP NAME"
shirtsOnly = True
pantsOnly = True
removeWatermark = True


def imgSaver(name, code):
	with open('output/' + name + '.png', 'wb') as f:
		f.write(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + code).text)['location']).content)

def watermarkRemover(name):
	mainImg = Image.open(r"output/" + name + ".png")
	template = Image.open(r"template.png") 
	mainImg.paste(template, (0,0), mask = template)
	mainImg.save("output/" + name + ".png")

def scanner(url):
	source = requests.get(url).text
	linkList = [url]
	urls = []
	nPC = json.loads(source)["nextPageCursor"]
	pattern = r"/?id=(.*?)</url>"

	while nPC != None:
		linkList.append(url + "&cursor=" + nPC)
		nPC = json.loads(requests.get(linkList[len(linkList)-1]).text)["nextPageCursor"]
		#print(nPC)
	#print(linkList)
	for link in linkList:
		for x in json.loads(requests.get(link).text)['data']:
			tempID = x['id']
			#print(tempID)
			mainUser = clean(sanitize_filepath(BeautifulSoup(requests.get("https://www.roblox.com/catalog/" + str(tempID)).text, 'html.parser').title.string.split('- Roblox')[0]),no_emoji=True,no_punct=True)
			#print(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text)
			#print(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text)
			code = re.search(pattern, requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text).group(1)
			#print(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + code).text)
			if removeWatermark == True:
				imgSaver(mainUser, code)
				watermarkRemover(mainUser)
			else:
				imgSaver(mainUser, code)


if shirtsOnly == True and pantsOnly == True:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicShirts")
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicPants")
elif shirtsOnly == False and pantsOnly == False:
	print("Please set shirtsOnly or pantsOnly to True")
elif shirtsOnly == False:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicPants")
elif pantsOnly == False:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicShirts")

