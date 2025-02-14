from flask import Flask
from src.routes.receipt_controller import receipt_bp

app = Flask(__name__)

@app.route("/")
def root_page():
    return "<h1>Receipt Processor API<h1>"

app.register_blueprint(receipt_bp)

if __name__ == '__main__':
    app.run()