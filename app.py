from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)


genai.configure(api_key="AIzaSyA5dJklf36OZl0SYT4yqBoR3M1l00hGz4s")


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
 
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.form.get('prompt')

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            },
            {
                "role": "model",
                "parts": ["Hi there! How can I help you today?\n"],
            },
        ]
    )
    
    response = chat_session.send_message(prompt)

    return jsonify({'status': 'success', 'generated_text': response.text})

if __name__ == '__main__':
    app.run(debug=True)
