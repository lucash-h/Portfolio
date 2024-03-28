from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])

def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = MIMEText(f'From: {name}\n{email}\n\n{message}')
    msg['Subject'] = 'New message from your website'
    msg['From'] = email
    msg['To'] = 'lhatelyhoneyman@gmail.com'

    s = smtplib.SMTP('smtp.gmail.com', 587)
    #pulling from environment variables
    s.login(os.environ['WebsiteEmailUsername'], os.environ['WebsiteEmailPassword'])
    s.send_message(msg)
    s.quit()

    return 'Message sent', 200



if __name__ == '__main__':
    app.run(debug=True)