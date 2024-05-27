from flask import Flask, render_template, request, g, redirect
import sqlite3
import requests
import math
import os
app = Flask(__name__)
database = 'datafile.db'


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(database)
    return g.sqlite_db


@app.teardown_appcontext
def close_connection(exception):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    result = cursor.execute("select * from cash")
    cash_result = result.fetchall()
    print(cash_result)
    # 計算台幣與美金總額
    taiwanese_dollars = 0
    us_dollars = 0
    for data in cash_result:
        print(type(data))
        taiwanese_dollars += data[1]
        us_dollars += data[2]
    # 獲取匯率資訊
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()
    total = math.floor(taiwanese_dollars + us_dollars *
                       currency['USDTWD']['Exrate'])

    print(currency)
    return render_template("index.html")


@app.route('/cash')
def cash_form():
    return render_template('cash.html')


@app.route('/cash', methods=['POST'])
def submit_cash():
    # 取得金額與日期資料
    taiwanese_dollars = 0
    us_dollars = 0
    if request.values['taiwanese-dollars'] != '':
        taiwanese_dollars = request.values['taiwanese-dollars']
    if request.values['us-dollars'] != '':
        us_dollars = request.values['us-dollars']
    note = request.values['note']
    date = request.values['date']

    # 更新數據庫資料
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""insert into cash (taiwanese_dollars, us_dollars, note, date_info) values (?, ?, ?, ?)""",
                   (taiwanese_dollars, us_dollars, note, date))
    conn.commit()
    # 將使用者導回主頁面
    return redirect("/")


@app.route('/stock')
def stock_form():
    return render_template("stock.html")


if __name__ == '__main__':
    app.run(debug=True)
