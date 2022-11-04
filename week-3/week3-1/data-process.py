import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

clist=data["result"]["results"]

with open("data.csv", "w", encoding="utf-8") as file:
    index=0
    for attractions in clist:
        if (attractions["xpostDate"])>=("2015/01/01"):
            site=attractions["file"]
            firstSite=(str(site.split("https:")[1]))
            file.write(attractions["stitle"] +","
            + attractions["address"][5:8] +","
            + attractions["longitude"] +","
            + attractions["latitude"] +","
            + "https:"+ firstSite +"\n"
            )
