from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_index.llms.openai import OpenAI
from scrapper import get_data
from cv_reader import read_cv

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/read-cv', methods=['POST'])
def read_cv_route():
    if 'cv' not in request.files:
        return jsonify({'error': 'No CV provided'}), 400
    file = request.files['cv']
    cv_data = read_cv(file)  # Function to read CV from the file
    return jsonify(cv_data)

@app.route('/get-job-data', methods=['POST'])
def get_job_data_route():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    job_data = get_data(url)  # Function to scrape job data from the URL
    return jsonify(job_data)

if __name__ == '__main__':
    app.run(debug=True)

