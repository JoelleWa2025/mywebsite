"""
Joelle Waugh's Portfolio Website
A clean, one-page Flask application showcasing cybersecurity student portfolio
"""
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET KEY'] = os.environ.get('adsakfdjakkldfjlsadjlfkaksdj')

# Routes
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False)