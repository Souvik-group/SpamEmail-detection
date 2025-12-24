from flask import Flask, render_template, request, jsonify
import pickle
import os
import warnings
import pandas as pd
import email
from email import policy
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'csv', 'eml'}

if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load model and vectorizer with error handling
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

try:
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    print("Vectorizer loaded successfully")
except Exception as e:
    print(f"Error loading vectorizer: {e}")
    vectorizer = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not loaded properly'})
    
    try:
        message = request.form['message']
        message_vec = vectorizer.transform([message])
        prediction = model.predict(message_vec)[0]
        probability = model.predict_proba(message_vec)[0].max()
        
        result = {
            'prediction': 'Spam' if prediction == 1 else 'Not Spam',
            'confidence': f"{probability:.2%}"
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'})

@app.route('/upload', methods=['POST'])
def upload_file():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not loaded properly'})
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    try:
        filename = file.filename.lower()
        
        if filename.endswith('.csv'):
            # Process CSV file
            df = pd.read_csv(file)
            
            if 'message' not in df.columns:
                return jsonify({'error': 'CSV must have a "message" column'})
            
            messages = df['message'].astype(str).tolist()
            
        elif filename.endswith('.eml'):
            # Process EML file
            file_content = file.read().decode('utf-8', errors='ignore')
            msg = email.message_from_string(file_content, policy=policy.default)
            
            # Extract email body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
            
            # Include subject in message
            subject = msg.get('Subject', '')
            full_message = f"{subject} {body}".strip()
            messages = [full_message]
            
        else:
            return jsonify({'error': 'Only CSV and EML files are supported'})
        
        # Process messages
        messages_vec = vectorizer.transform(messages)
        predictions = model.predict(messages_vec)
        probabilities = model.predict_proba(messages_vec)
        
        results = []
        for i, (msg, pred, prob) in enumerate(zip(messages, predictions, probabilities)):
            results.append({
                'row': i + 1,
                'message': msg[:100] + '...' if len(msg) > 100 else msg,
                'prediction': 'Spam' if pred == 1 else 'Not Spam',
                'confidence': f"{prob.max():.2%}"
            })
        
        spam_count = sum(1 for pred in predictions if pred == 1)
        total_count = len(predictions)
        
        return jsonify({
            'results': results,
            'summary': {
                'total': total_count,
                'spam': spam_count,
                'not_spam': total_count - spam_count
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'File processing failed: {str(e)}'})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
