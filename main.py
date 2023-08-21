from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time, requests, json
from cleantext import clean

def selenium_script():
	URL = "GROUPALLCLOTHESLINK"
	IDs = []
	names = []
	IDsDict = {}
	driver = webdriver.Chrome()
	driver.implicitly_wait(6)
	driver.get(URL)
	mainSec = driver.find_element(By.CSS_SELECTOR, '.hlist.item-cards-stackable.ng-scope')
	elementList = mainSec.find_elements(By.CLASS_NAME , 'item-card-container')
	for x in elementList:
		# Select the <a> tag within the div

		link_element = x.get_attribute('href').split('/')
		print(link_element)
		xStr = x.text[0:x.text.find("By ")]
		if len(link_element) == 1:
			pass
		else:
			names.append(xStr)
			num = link_element[4]
			IDs.append(num)
			IDsDict.update({num: xStr})
	time.sleep(1)
	for x in IDsDict:
		driver.get("https://assetdelivery.roblox.com/v1/assetId/" + x)
		mainSTR = driver.find_element(By.XPATH, "/html/body/pre").text
		link = str(json.loads(mainSTR)["location"])
		try:
			pngID = str(requests.get(link).content).split('<url>http://www.roblox.com/asset/?id=')[1].split('</url>')[0]
			driver.get("https://assetdelivery.roblox.com/v1/assetId/" + pngID)
			mainSTR = driver.find_element(By.XPATH, "/html/body/pre").text
			link = str(json.loads(mainSTR)["location"])
			with open(f'output/{clean(IDsDict.get(x), no_emoji=True)}.png', 'wb') as f:
				f.write(requests.get(link).content)
		except IndexError:
			print("not pants or shirt")
		
if __name__ == "__main__":
	selenium_script()