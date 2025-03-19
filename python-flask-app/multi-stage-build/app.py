from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Flask App</title>
    </head>
    <body>
        <h1>Welcome to Flask App</h1>
        <p>This is a HTML page generated using Python and Flask.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)