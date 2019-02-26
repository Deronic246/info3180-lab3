from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '340d9b5ea8ae7b'
app.config['MAIL_PASSWORD'] = '5c6a655a3cc872'
mail = Mail(app)
from app import views