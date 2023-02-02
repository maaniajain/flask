from bs4 import BeautifulSoup


file = open("C:/Users/jaind/PycharmProjects/webscrap3/morenews",mode='r')
data = file.read()
# all = []
# def zee_news_data():
MORE_NEWS_SELECTOR ="body > div.container.catergory-section-container > div > div.col-md-9 > div.more-news-section"
soup = BeautifulSoup(str(data),"html.parser")
more_news_all = soup.select(MORE_NEWS_SELECTOR)
soup = BeautifulSoup(str(more_news_all),"html.parser")
new_news= soup.find("div")
print(soup.text)
exit()

# count =0
# count2 = 0
# all = []
# for i in new_news:
#     if count <= 0:
#         count = count + 1
#         continue
#     count = count + 1
#     soup = BeautifulSoup(str(i), "html.parser")
#     special_news = soup.find("div")
#          for j in special_news:
#              if
    # print(special_news)
    # # if len(special_news) >=2:
    # #     data={
    # #         "headline": speacial_news[1].text
    # #     }





    # print(i)
    # soup = BeautifulSoup(str(i), "html.parser")
    # train_details = soup.findAll("div")
    # if len(train_details) >= 2:
    #     data = {
    #         "train_no": train_details[1].text,
    #     }