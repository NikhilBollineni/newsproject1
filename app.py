from flask import Flask, jsonify
from gnews import GNews
import json
import os

app = Flask(__name__, static_folder="static", static_url_path="")

INDUSTRIES = [
    "finance",
    "hvac",
    "automotive",
    "technology",
    "sports",
]

news_dir = "news"
os.makedirs(news_dir, exist_ok=True)

gnews = GNews()


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/industries")
def industries():
    return jsonify(INDUSTRIES)


@app.route("/news/<industry>")
def news(industry: str):
    if industry not in INDUSTRIES:
        return jsonify({"error": "unknown industry"}), 404
    articles = gnews.get_news(industry)
    file_path = os.path.join(news_dir, f"{industry}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    return jsonify(articles)


if __name__ == "__main__":
    app.run(debug=True)
