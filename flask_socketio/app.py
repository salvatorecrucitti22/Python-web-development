from flask import Flask, render_template
from flask_socketio import SocketIO
import time
app = Flask(__name__)
socket = SocketIO(app)
li = [1,2,3,4,5]
i=0
@app.route('/')
def main():
    return render_template('index.html')

@socket.on('message')
def handlemss(msg):
    global i
    if i < len(li):
        time.sleep(10)
        socket.send(li[i])
        i+=1

if __name__ == "__main__":
    socket.run(app)

