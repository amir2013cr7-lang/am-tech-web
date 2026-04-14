from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Email configuration
RECIPIENT_EMAIL = "amir2013.cr7@gmail.com"
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'amir2013@gmail.com')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD','')
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

@app.route('/')
def index():
    return send_from_directory('.', 'code.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['name', 'email', 'message']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        message = data['message'].strip()
        
        if not name or not email or not message:
            return jsonify({'error': 'All fields are required'}), 400
        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Contact Form Submission from {name}"
        
        # Email body
        body = f"""
New Contact Form Submission
==========================

Name: {name}
Email: {email}
Message:
{message}

---
This message was sent from your AM Tech website contact form.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({'error': f'Failed to send email: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
