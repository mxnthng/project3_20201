from newspaper import Article
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

turl = [
    "https://vnexpress.net/hlv-park-keu-goi-co-hoi-cho-tien-dao-viet-nam-4212615.html",
    "https://vnexpress.net/tai-xe-tu-vong-khi-dang-cach-ly-y-te-4212610.html",
    "https://vnexpress.net/hai-nu-sinh-bi-danh-tren-duong-4212609.html"
]

urlss = "https://vnexpress.net"
i = 0
j = 0
k = 0
check = True
while check:
    i += 1
    file = open("text{}.txt".format(i), "a+")
    print("Open file: {}".format(i))
    while True:
        try:
            if j >= len(turl):
                check = False
                file.close()
                break

            url = turl[j]
            if url[0:4] != "http":
                url = urlss + url

            req = Request(url)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            for link in soup.findAll('a'):
                link1 = link.get('href')
                if link1 and len(link1) > 5 and link1[len(link1) - 5:] == ".html" and link1 not in turl:
                    turl.append(link1)

            article = Article(url)
            article.download()
            article.parse()
            file.write(article.text)

            print("({}) - {} - Crawl url: {}".format(j, k, url))

            j += 1
            k += 1
            if k >= 5000:
                print("Close file: 1text{}.txt".format(i))
                k = 0
                file.close()
                break
        except Exception as e:
            print(e)
            j += 1

