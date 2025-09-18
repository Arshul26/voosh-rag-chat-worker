from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import os

app = Flask(__name__)

# smaller model chosen earlier
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/embed", methods=["POST"])
def embed():
    data = request.json
    text = data.get("text") or data.get("texts")
    if isinstance(text, list):
        vecs = model.encode(text).tolist()
        return jsonify({"embeddings": vecs})
    vec = model.encode(text).tolist()
    return jsonify({"embedding": vec})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(port=port, host="0.0.0.0")
