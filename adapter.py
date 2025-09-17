from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Use a smaller model to reduce memory usage
# This uses ~200MB instead of 400-500MB
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

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
    # Render requires PORT from env, default to 5001 if not set
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(port=port, host="0.0.0.0")



