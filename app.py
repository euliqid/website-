from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page with the image and buttons
    return render_template('index.html')

@app.route('/correct')
def correct():
    # Render the "correct" page when the correct button is clicked
    return render_template('correct.html')

@app.route('/wrong')
def wrong():
    # Render the "wrong" page when an incorrect button is clicked
    return render_template('wrong.html')

if __name__ == '__main__':
    app.run(debug=True)
