import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '這是我在雲端的第一個 Python 程式！'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 從環境變數抓 PORT（預設 5000）
    app.run(host='0.0.0.0', port=port)
