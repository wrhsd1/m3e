from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

m3e = SentenceTransformer('moka-ai/m3e-base')

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask on Debian 11!"

@app.route('/v1/embeddings', methods=['POST'])
def embeddings():
    data = request.json
    input_text = data.get('input')
    model = data.get('model')
    if model is None:
        model = "moka-ai/m3e-base"

    if input_text is None:
        return jsonify(error="No input text provided"), 400

    if isinstance(input_text, str):
        sentences = [input_text]
    elif isinstance(input_text, list):
        sentences = input_text

    embeddings = m3e.encode(sentences)
    embeddings = embeddings.tolist()
    data = [{"object": "embedding", "embedding": x, "index": i} for i, x in enumerate(embeddings)]

    response = {
        "object": "list",
        "data": data,
        "model": model,
        "usage": {
            "prompt_tokens": 0,
            "total_tokens": 0
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
