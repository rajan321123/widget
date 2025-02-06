from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    bot_response = f"Hello! You said: {user_input}"  # Replace with AI logic
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
