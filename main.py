import requests, json, re, random
from bs4 import BeautifulSoup
from cleantext import clean
from urllib.parse import quote
from pathvalidate import sanitize_filepath


groupName = "GROUP NAME"
shirtsOnly = False
pantsOnly = True

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
		print(json.loads(requests.get(link).text)['data'])
	for link in linkList:
		for x in json.loads(requests.get(link).text)['data']:
			tempID = x['id']
			#print(tempID)
			mainUser = clean(sanitize_filepath(BeautifulSoup(requests.get("https://www.roblox.com/catalog/" + str(tempID)).text, 'html.parser').title.string.split('- Roblox')[0]),no_emoji=True,no_punct=True)
			#print(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text)
			#print(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text)
			code = re.search(pattern, requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + str(x['id'])).text)['location']).text).group(1)
			#print(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + code).text)
			with open('output/' + mainUser + '.png', 'wb') as f:
				f.write(requests.get(json.loads(requests.get("https://assetdelivery.roblox.com/v1/assetId/" + code).text)['location']).content)
	return urls

if shirtsOnly == True and pantsOnly == True:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicShirts")
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicPants")
elif shirtsOnly == False and pantsOnly == False:
	print("Please set shirtsOnly or pantsOnly to True")
elif shirtsOnly == False:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicPants")
elif pantsOnly == False:
	scanner("https://catalog.roblox.com/v1/search/items?category=Clothing&creatorName=" + quote(groupName) + "&creatorType=Group&limit=120&salesTypeFilter=1&subcategory=ClassicShirts")
