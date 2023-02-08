from flask import *
from webbrowser import *

server = Flask(__name__)

@server.route('/')
def home():
    return send_file('public/index.html')

@server.route('/downloads/')
def downloads():
    return send_file("public/download.html")

@server.route('/download/source-code')
def downloadsource():
    return redirect('https://github.com/Nintal-org/Nintal')

@server.route('/getting-started')
def g():
    return redirect('https://youtube.com/')
@server.route('/docs')
def docs():
    return send_file('public/docs/docs.html')

if __name__ == "__main__":
    server.run(host="localhost",port=5050)
