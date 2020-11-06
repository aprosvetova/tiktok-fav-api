from flask import Flask, jsonify
from TikTokApi import TikTokApi

api = TikTokApi()
app = Flask(__name__)


@app.route('/user/<username>')
def get_liked(username):
    try:
        likes = api.userLikedbyUsername(username)
        return jsonify([v['id'] for v in likes])
    except Exception as e:
        return jsonify({'error': repr(e)}), 500


app.run(port=80)
