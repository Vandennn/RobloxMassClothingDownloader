# RobloxMassClothingDownloader
Script to auto download an entire groups clothing (Shirts and Pants)

# Setup
To set this up run "pip -r requirements.txt"

Once you install all of the requirements, Selenium, atleast for me seems to be buggy if I keep the main.py file inside of a subfolder, so if you plan to keep it in a subfolder then make sure to drag and drop the chromedriver.exe file into the same folder. If you don't, i.e. simply keeping the main.py in the downloads folder for example then just install the requirements.

# Configuration
For configuration, just replace the URL variable with the groups ***SEE ALL*** page. Not just their group link. When you look at a groups store there should be a button called **See All ->**.

Once you are on the See All page copy the link which should look something like this: __https://www.roblox.com/catalog?Category=1&CreatorName=Aesthetic%20Aethers&CreatorType=Group__

After you have set your link run the script and it will download all of the clothes.

# Features
Auto-download multiple roblox shirts and pants at a time

Saved clothing template will have shirt name set as it automatically (no need to name while uploading)

Very quick for downloading (if you aren't rate-limited)

# Credit
While most of this script was mainly created by me, I did not create the section of code that grabs the jpg clothing image.
That section was written by jedpep on his own roblox clothing downloader: __https://github.com/jedpep/Roblox-Mass-Clothing-Stealer__
