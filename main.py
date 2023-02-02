from flask import Flask
app = Flask(__name__)
import test
import db
import zee_news
@app.route('/test')
def hello_world():
    data = test.studentdetails()
    test.save_data_to_db(data)
    return data

@app.route('/zee_news')
def zee_news_latest():
    data = zee_news.zee_news_data()
    zee_news.save_date_to_db(data)
    return data

@app.route('/more_news')
def zee_more_news():
    data = zee_news.more_news()
    return data

@app.route('/get_data')
def get_data():
    db_curser = db.mycursor
    db_curser.execute('select * from zee_news where tital like "%Bigg%"')
    data = db_curser.fetchall()
    data_to_send = []
    for i in data:
        data_to_send.append({
            "id" : i[0],
            "href" : i[1],
            "text" : i[2],
            "title" :i[3]
        })

    return data_to_send

if __name__ == '__main__':
    app.run()