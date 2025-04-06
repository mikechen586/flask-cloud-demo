from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '這是我在雲端的第一個 Python 程式！'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
