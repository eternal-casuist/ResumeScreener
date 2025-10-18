
from flask import Flask, render_template, request
import os
from ml_model import extract_text_from_pdf, compute_similarity

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    job_desc = request.form['job_description']

    file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)

    resume_text = extract_text_from_pdf(file_path)
    score = compute_similarity(resume_text, job_desc)

    return render_template('result.html', score=score)

if __name__ == "__main__":
    app.run(debug=True)
