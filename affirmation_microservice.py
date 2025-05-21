from flask import Flask, request, jsonify
import random

app = Flask(__name__)


affirmations = {
    "happy": [
        "Glad to hear!",
        "We're happy that you're happy!"
    ],
    "sad": [
        "Sorry to hear you’re feeling down.",
        "Sending you a virtual hug!"
    ],
    "anxious": [
        "You're doing your best, and that's enough.",
        "Take a breath, you’ve got this!",
    ],
    "angry": [
        "Take a moment to cool down. You’ve got this.",
        "Breathe deeply and let it go."
    ]
}


@app.route('/get_affirmation', methods=['POST'])
def get_affirmation():
    data = request.get_json()
    mood = data.get('mood', '').lower()

    if mood in affirmations:
        affirmation = random.choice(affirmations[mood])
        return jsonify({"affirmation": affirmation}), 200
    else:
        return jsonify({"error": "Mood not recognized"}), 400

if __name__ == '__main__':
    app.run(debug=True)