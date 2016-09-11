import pandas as pd
from lxml import html
import re
import requests

site = raw_input("Input bandcamp release page.")
name_get = re.search("https:\/\/(?:.*).bandcamp.com\/album\/(.*)", site)
name = name_get.group(1)


page = requests.get(site)
tree = html.fromstring(page.content)

tracks = tree.xpath('//table[@id ="track_table"]//td[@class="title-col"]/div[@class="title"]/a/span/text()')
time = tree.xpath('//table[@id ="track_table"]//td[@class="title-col"]/div[@class="title"]/span/text()')
newtimes = []

for item in time:
    newitem = item.strip()
    newtimes.append(newitem)

raw_data = {"track": tracks, "time": newtimes}

df = pd.DataFrame(raw_data, columns = ["track", "time"])

df.index += 1

df.to_csv(raw_input("Input the csv path. Default ~/NameOfAlbum.csv.") or "~/" + name.encode('utf-8') + ".csv")
