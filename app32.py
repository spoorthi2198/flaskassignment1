from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('notify.html')

@app.route('/send')
def notify_all():
    message = request.args.get('msg', 'Hello, all users!')
    socketio.emit('notify', {'message': message})
    return "Notification sent!"

if __name__ == '__main__':
    socketio.run(app, debug=True)
