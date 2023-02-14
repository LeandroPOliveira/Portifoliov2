import os
from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'lambreta'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['user'],
    "MAIL_PASSWORD": os.environ['senha']
}

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)