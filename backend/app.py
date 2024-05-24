from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import requests
import os

app = Flask(__name__)
CORS(app) # Enable CORS for the API

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

def fetch_and_extract_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])
        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the content you are provided."},
            {"role": "user", "content": text},
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
    )

    summary = response.choices[0].message.content.strip()
    return summary

@app.route('/summarize', methods=['POST'])
def summarize_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    text_content = fetch_and_extract_text(url)
    if not text_content:
        return jsonify({"error": "Unable to fetch or extract text from the URL"}), 500
    
    summary = summarize_text(text_content)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
