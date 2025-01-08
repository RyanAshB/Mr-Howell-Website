from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

if __name__ == '__main__':
    app.run()
