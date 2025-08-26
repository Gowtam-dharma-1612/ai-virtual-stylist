from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Demo stub: replace with real logic ---
def recommend_outfits(image_path: str):
    # TODO: call utils.image_processing functions and ML models
    # Dummy response structured for recruiters to see:
    return {
        "user_attributes": {"body_type": "mesomorph", "skin_tone": "medium", "gender": "unisex"},
        "recommendations": [
            {"top": "solid crew-neck tee", "bottom": "slim-fit chinos", "shoes": "white sneakers"},
            {"top": "light denim shirt", "bottom": "black jeans", "shoes": "boots"}
        ],
        "notes": "This is a stub. Replace with model-driven recommendations."
    }

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json(force=True)
    image_path = data.get("image_path", "")
    if not image_path:
        return jsonify({"error": "image_path required"}), 400
    result = recommend_outfits(image_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
