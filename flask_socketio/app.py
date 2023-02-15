from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
li = [1,2,3,4,5]
@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

