import random
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample word list for random generation
WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation",
    "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat"
]

def generate_text(length, text_type="word"):
    if text_type == "word":
        return " ".join(random.choice(WORDS) for _ in range(length))
    elif text_type == "sentence":
        return ". ".join(" ".join(random.choice(WORDS) for _ in range(8)) for _ in range(length)) + "."
    elif text_type == "paragraph":
        return "\n\n".join(". ".join(" ".join(random.choice(WORDS) for _ in range(8)) for _ in range(5)) + "." for _ in range(length))
    else:
        return "Invalid type specified."

# Route to check if the system is working
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "System is working properly!"})

# Route to generate random text
@app.route('/generate', methods=['GET'])
def generate_random_text():
    length = int(request.args.get('length', 10))  # Default length 10
    text_type = request.args.get('type', 'word')  # Default type is 'word'
    random_text = generate_text(length, text_type)
    return jsonify({"text": random_text})

if __name__ == "__main__":
    app.run(debug=True)
