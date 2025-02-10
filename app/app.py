from flask import Flask

app = Flask(__name__)

@app.route("/")
def app_home():
    return "<p>recipt-processor-api/p>"