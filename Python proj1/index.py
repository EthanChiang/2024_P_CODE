from flask import Flask, jsonify, render_template, request, g, redirect
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
    # print(cash_result)
    # 計算台幣與美金總額
    taiwanese_dollars = 0
    us_dollars = 0
    for data in cash_result:
        # print(type(data))
        taiwanese_dollars += data[1]
        us_dollars += data[2]
    # 獲取匯率資訊
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()
    total = math.floor(taiwanese_dollars + us_dollars *
                       currency['USDTWD']['Exrate'])
    data = {'total': total, 'td': taiwanese_dollars,
            'ud': us_dollars, 'currency': currency['USDTWD']['Exrate'], 'cash_result': cash_result}
    # print(currency)
    return render_template("index.html", data=data)


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


@app.route('/cash-delete', methods=['POST'])
def delete():
    transcation_id = request.values['id']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""delete from cash where transaction_id=?""",
                   (transcation_id,))
    conn.commit()
    return redirect("/")


@app.route("/stock")
def stock():
    return render_template("stock.html")


@app.route('/stock', methods=["POST"])
def stock_form():
    stock_id = request.values['stock-id']
    stock_num = request.values['stock-num']
    stock_price = request.values['stock-price']
    processing_fee = 0
    tax = 0
    if request.values['processing-fee'] != '':
        processing_fee = request.values['processing-fee']
    if request.values['tax'] != '':
        tax = request.values['tax']
    date = request.values['date']
    print(stock_id, stock_num, stock_price, processing_fee, tax)
    # 更新數據庫資料
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""insert into stock (stock_id, stock_num, stock_price, processing_fee, tax, date_info) values (?, ?, ?, ?, ?, ?)""",
                   (stock_id, stock_num, stock_price, processing_fee, tax, date))
    conn.commit()
    # 將使用者導回主頁面
    return redirect('/')


@app.route('/stock', methods=["POST"])
def submit_stock():

    return render_template("stock.html")


@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    return render_template("test.html", name2=name)


@app.route("/info", methods=["POST"])
def ruturnSomething():
    # JavaScript Object Notation
    return jsonify({"info": "you have successfully make a request"})


if __name__ == '__main__':
    app.run(debug=True)
