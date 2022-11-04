import urllib.request as req
def getData(url, headline):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    with open("movie.txt","a",encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                if title.a.string[0:4] == headline: 
                    file.write(title.a.string+"\n")

    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]
    
pageURL="https://www.ptt.cc/bbs/movie/index.html"

with open("movie.txt", "w", encoding= "utf-8") as file:
    page=0   
    while page<10:
        pageURL="https://www.ptt.cc"+getData(pageURL, "[好雷]")
        page+=1
    page=0
    while page<10:
        pageURL="https://www.ptt.cc"+getData(pageURL, "[普雷]")
        page+=1
    page=0
    while page<10:
        pageURL="https://www.ptt.cc"+getData(pageURL, "[負雷]")
        page+=1
