from bs4 import BeautifulSoup
import db


def zee_news_data():
    file = open("C:/Users/jaind/PycharmProjects/webscrap3/latest-news", mode='r')
    data = file.read()
    LATEST_NEWS_SELECTOR = "body > div.container.catergory-section-container > div > div.col-md-9 > div.row.no-gutters"
    soup = BeautifulSoup(str(data), "html.parser")
    latest_news_all = soup.select(LATEST_NEWS_SELECTOR)

    soup = BeautifulSoup(str(latest_news_all), "html.parser")
    new_news = soup.findAll("li")
    data_to_send =[]
    for i in new_news:
        soup = BeautifulSoup(str(i), "html.parser")
        newline = soup.find("a")
        data= {
            "href":newline["href"],
            "title": newline["title"],
            "text": i.text
        }
        data_to_send.append(data)
    return data_to_send

def more_news():

    file = open("C:/Users/jaind/PycharmProjects/webscrap3/latest-news", mode='r')
    data = file.read()
    MORE_NEWS_SELECTOR = "body > div.container.catergory-section-container > div > div.col-md-9 > div.more-news-section"
    soup = BeautifulSoup(str(data), "html.parser")
    more_news_all = soup.select(MORE_NEWS_SELECTOR)
    soup = BeautifulSoup(str(more_news_all), "html.parser")
    new_news = soup.findAll("div")
    count = 0
    data_to_live =[]
    for i in new_news:
        if count == 2:
            continue
        soup = BeautifulSoup(str(i), "html.parser")
        newline = soup.find("a")
        soup = BeautifulSoup(str(i), "html.parser")
        date = soup.find("div")
        if newline == None:
            continue
        # print("newline",newline)
        data= {
                "href":newline["href"],
                "title": newline["title"],
                "text": i.text,
                "date": date.text
            }
        data_to_live.append(data)
    return data_to_live


def save_date_to_db(news_data):
    query = "INSERT INTO `zee_news` (`id`, `href`, `text`, `tital`) VALUES "
    for news in news_data:
        query = query+" (NULL,'"+news['href']+"','"+news['text']+"','"+news['title']+"'),"
    query = query[:len(query)-1]
    db_curser = db.mycursor
    db_curser.execute(query)
    db.mydb.commit()

#         data_to_live.append(data)
#     return data_to_live