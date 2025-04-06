from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '期指操作系統 v1'

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.json
    events = body.get('events', [])
    for event in events:
        if event['type'] == 'message':
            user_id = event['source']['userId']
            print(f"你收到訊息來自 userId：{user_id}")
            return jsonify({'status': 'ok', 'userId': user_id})
    return jsonify({'status': 'no message'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
