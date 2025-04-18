from flask import Flask, request, jsonify
from core import extract_keywords
app = Flask(__name__)

@app.route('/tags', methods=['POST'])
def get_tags():
    data = request.json
    blog_text = data.get("text", "")
    tags = extract_keywords(blog_text)
    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(debug=True)
