from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = f"Echo: {user_input}"  # Replace with AI-generated response
    return jsonify({"reply": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
