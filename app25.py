from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/cause-error')
def cause_error():
    return 1 / 0  # triggers 500 error

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Error - Page Not Found</h1>", 404

@app.errorhandler(500)
def server_error(e):
    return "<h1>500 Error - Internal Server Error</h1>", 500

if __name__ == '__main__':
    app.run(debug=True)
