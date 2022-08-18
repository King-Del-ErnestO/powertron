from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

