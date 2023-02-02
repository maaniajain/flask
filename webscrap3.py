import requests
from bs4 import BeautifulSoup

train_url ="https://indiarailinfo.com/train/1459"

TRAINS_CSS_SELECTOR = '#MainBody'
def fetch_response(url):
    response = requests.get(url)
    return response.text

def fetch_all_trains(content):
    soup = BeautifulSoup(str(content),"html.parser")
    data_text = soup.select(TRAINS_CSS_SELECTOR)
    soup = BeautifulSoup(str(data_text),"html.parser")
    train_box= soup.findAll('div')
    count = 1
    all = []
    for i in train_box:
        if count == 0:
            count = count + 1
            continue
        count = count + 1
        soup = BeautifulSoup(str(i), "html.parser")
        train_details = soup.findAll("div")
        soup = BeautifulSoup(str(i), "html.parser")
        i = soup.findAll('div')
        count2 = 1
        count3 = 0
        all = []
        for j in train_details:
            if count2 <= 315:
               count2 = count2 + 1
               continue

            count3 = count3 + 1
            if  count3 == 10:
                print(j.text)
                count3 = 0;



            print(j.text)


    return all


response = fetch_response(train_url)
print(fetch_all_trains(response))