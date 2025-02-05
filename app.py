from flask import Flask, request, jsonify
import requests  # Importing requests to interact with external APIs

app = Flask(__name__)

# Set your Gore API endpoint and API key here (replace with actual endpoint and API key)
GORE_API_URL = "https://api.goreapi.com/chat"  # Example URL, replace with actual Gore API endpoint
GORE_API_KEY = "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"  # Replace with your actual Gore API key

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Getting message from the request payload
        data = request.json
        user_message = data.get("message")

        # Define the payload for the API request
        payload = {
            "message": user_message,
            "api_key": GORE_API_KEY
        }

        # Make an HTTP POST request to the Gore API
        response = requests.post(GORE_API_URL, json=payload)

        # If the request is successful, return the response
        if response.status_code == 200:
            api_response = response.json()
            return jsonify({"response": api_response.get("response")})

        # If the response is not successful, return an error message
        return jsonify({"error": "Failed to get response from Gore API"}), 500

    except Exception as e:
        # Catch any exceptions and return an error message
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
