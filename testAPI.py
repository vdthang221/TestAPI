from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  # Load biến từ .env file

app = Flask(__name__)
CORS(app)  # Allow requests từ HTML

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Lấy từ .env

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    msg = data.get('message', '')
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": msg}]
    )
    
    return jsonify({
        "reply": response.choices[0].message.content
    })

if __name__ == '__main__':
    print("🚀 Groq Chat running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)