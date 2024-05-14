import requests
from bs4 import BeautifulSoup
import pandas as pd


news_list = []

response = requests.get('https://akharinkhabar.ir/sport')
page = BeautifulSoup(response.content, "html.parser")
# print(page.find_all( "div","title"))
for link in page.find_all("a"):
        try:

                print(link["href"])
                print(link.text)
                print(link.date)
                news = {"link": link["href"], "data" : link.date , "title" : link.text }
                news_list.append(news)
        except :
                pass
# try:
#         # title , link , date = option.text
#         title = title.strip()
#         news = {"Title ": title , "link" : link , "date" : date}
#         news_list.append(news)
#         # print(page)
# except :
#         pass
# print(response.text)
df = pd.DataFrame(news_list)
df.to_csv("news.csv" , index=False)


