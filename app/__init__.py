from flask import Flask

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<h1>Receipt Processor API<h1>"

    # Register routes
    from app.routes.receipt_controller import receipt_bp
    app.register_blueprint(receipt_bp)

    return app