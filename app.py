from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return "ICS Generator API is running!"

@app.route('/generate-ics', methods=['POST'])
def generate_ics():
    data = request.json
    ocr_text = data.get("ocr_text")

    prompt = f"""You are a calendar assistant. Convert the following text into an .ics calendar event.
Only return the raw .ics file content.

Text:
{ocr_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=800
    )

    ics_text = response.choices[0].message['content']
    return jsonify({"ics_text": ics_text})
