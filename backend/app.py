from flask import Flask, request, jsonify
from flask_cors import CORS
from scrapper import get_data
from cv_reader import read_cv, retrieve_relevant_info
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
        # Save the uploaded file temporarily if read_cv() needs a file path
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        # Read and embed the CV from the temporary file path
        cv_index = read_cv(temp_path)

        if not cv_index:
            return jsonify({'error': 'Failed to process CV on flask'}), 500

        insights_query = "Summarize this CV and highlight key skills."
        insights = retrieve_relevant_info(cv_index, insights_query)

        return jsonify({
            'message': 'CV successfully processed',
            'insights': insights
        })

    except Exception as e:
        print(f"❌ Error processing CV: {e}")
        return jsonify({'error': f'Failed to process CV: {str(e)}'}), 500


@app.route('/get-job-data', methods=['POST'])
def get_job_data_route():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    job_data = get_data(url)  # Function to scrape job data from the URL

    if not job_data:
        return jsonify({'error': 'Failed to retrieve job data'}), 500

    return jsonify(job_data)

if __name__ == '__main__':
    app.run(debug=True)
