from flask import Flask, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# Set your Gorq API Key
gorq_api_key = "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"
GORQ_API_URL = "https://api.gorq.com/chat"

# Chatbot API endpoint
@app.route('/chat/', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400

        headers = {"Authorization": f"Bearer {gorq_api_key}", "Content-Type": "application/json"}
        payload = {"message": message}
        response = requests.post(GORQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        reply = response.json().get("response", "No response from Gorq API")
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Root endpoint
@app.route('/')
def root():
    return jsonify({"message": "Chatbot backend is running!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
