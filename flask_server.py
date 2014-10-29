# coding: utf-8

from flask import Flask, request, render_template

import checker

app = Flask(__name__)


@app.route('/')
def index():
    input_url = request.values.get('input_url', '')
    correct_price = request.values.get('correct_price', '')
    retry_times = int(request.values.get('retry_times', '16'))

    results = []
    if input_url:
        item_url = checker.get_item_url(input_url)
        sib_url = checker.get_sib_url(item_url)
        results = checker.fetch_taobao_price(sib_url, item_url, retry_times)

    return render_template('checker.html', results=results, input_url=input_url, correct_price=correct_price)

if __name__ == "__main__":
    app.run('0.0.0.0', 9960)
