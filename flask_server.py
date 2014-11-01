# coding: utf-8

from flask import Flask, request, render_template

from actions import checker

app = Flask(__name__)


@app.route('/')
def index():
    input_url = request.values.get('input_url', '')
    retry_times = int(request.values.get('retry_times', '16'))

    results = []
    if input_url:
        item_url = checker.get_item_url(input_url)
        results = checker.fetch_taobao_price(item_url, retry_times)

    return render_template('checker.html', results=results)

if __name__ == "__main__":
    app.run('0.0.0.0', 9960)
