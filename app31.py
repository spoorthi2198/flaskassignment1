from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('update.html')

def background_thread():
    count = 0
    while True:
        time.sleep(2)
        count += 1
        socketio.emit('update', {'number': count})

@socketio.on('connect')
def on_connect():
    print("Client connected")
    threading.Thread(target=background_thread).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
