from flask import Flask, request, jsonify
from flask_cors import CORS
from scrapper import get_data
from cv_reader import read_cv, retrieve_relevant_info
from ai_insights import get_insights
import tempfile

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for all domains (allows frontend to interact with backend)
cv_index = None  

# -------------------------------
# Route to Process and Read CV
# -------------------------------

@app.route('/read-cv', methods=['POST'])
def read_cv_route():
    global cv_index  # Use the global variable to store the processed CV

    # Check if a file is included in the request
    if 'cv' not in request.files:
        return jsonify({'error': 'No CV provided'}), 400

    file = request.files['cv']

    try:
        # Save the uploaded CV file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        # Process the CV and generate embeddings
        cv_index = read_cv(temp_path)

        # If CV processing fails, return an error
        if not cv_index:
            return jsonify({'error': 'Failed to process CV'}), 500

        # Extract relevant information from the CV
        insights = retrieve_relevant_info(cv_index)

        # Return the extracted insights
        return jsonify(insights)

    except Exception as e:
        # Return error if insights retrieval fails
        return jsonify({'error': f'Failed to process CV: {str(e)}'}), 500 


# ----------------------------------
# Route to Fetch Job Description Data
# ----------------------------------

@app.route('/get-job-data', methods=['POST'])
def get_job_data_route():
    data = request.get_json()  # Parse incoming JSON data

    url = data.get('url')  # Extract job posting URL

    # Ensure a URL is provided
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Scrape job data from the provided URL
        job_data = get_data(url)
        # Return the job data
        return jsonify(job_data)

    except Exception as e:
        # Return error if job data retrieval fails
        return jsonify({'error': str(e)}), 500


# --------------------------------------
# Route to Get AI-Powered CV Insights
# --------------------------------------

@app.route('/get-ai-insights', methods=['POST'])
def get_ai_insights_route():
    request_data = request.get_json()  # Parse incoming JSON request

    cv_data = request_data.get('cvData')  # Extract CV-related data
    job_data = request_data.get('jobData')  # Extract job-related data

    # Ensure both CV and job data are provided
    if not cv_data or not job_data:
        return jsonify({'error': 'Both CV data and job data are required'}), 400

    try:
        # Generate AI-driven insights based on CV and job data
        insights = get_insights(cv_data, job_data)
        
        # Return the insights as a JSON response
        return jsonify(insights)

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Handle errors gracefully
