from flask import Flask, request, jsonify
from flask_cors import CORS
from scrapper import get_data
from cv_reader import read_cv, retrieve_relevant_info
from ai_insights import get_insights
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Store the CV embeddings in memory
cv_index = None

@app.route('/read-cv', methods=['POST'])
def read_cv_route():
    global cv_index

    if 'cv' not in request.files:
        return jsonify({'error': 'No CV provided'}), 400

    file = request.files['cv']

    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        # Read and embed the CV from the temporary file path
        cv_index = read_cv(temp_path)

        if not cv_index:
            return jsonify({'error': 'Failed to process CV'}), 500

        insights = retrieve_relevant_info(cv_index)

        return jsonify(insights)

    except Exception as e:
        print(f"Error processing CV: {e}")
        return jsonify({'error': f'Failed to process CV: {str(e)}'}), 500


@app.route('/get-job-data', methods=['POST'])
def get_job_data_route():
    data = request.get_json()

    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        job_data = get_data(url)
        return jsonify(job_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-ai-insights', methods=['POST'])
def get_ai_insights_route():
    request_data = request.get_json()

    cv_data = request_data.get('cvData')
    job_data = request_data.get('jobData')

    # Check if both cv_data and job_data are provided
    if not cv_data or not job_data:
        return jsonify({'error': 'Both CV data and job data are required'}), 400
    
    try:
        # Get AI insights by passing cv_data and job_data to the get_insights function
        insights = get_insights(cv_data, job_data)
        
        # Return the insights as a response
        return jsonify(insights)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
