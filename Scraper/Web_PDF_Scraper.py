# download pdf files from a hosted site

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = r"https://tobychristie.com/racing-series/nascar-cup-series/2022-loop-data/"

#If there is no such folder, the script will create one automatically
folder_location = r'C:\Users\kchen\OneDrive\MADS\SIADS591_592_Milestone1\Milestone_I\data\loop_TobyChristie\pdf\2022'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)