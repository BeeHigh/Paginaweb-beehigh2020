from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('iniciob.html')

@app.route('/otro')
def otro():
    return otro

if __name__== '__main__':
    app.run(debug=True)
