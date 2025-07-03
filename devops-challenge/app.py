from flask import Flask
from routers.health_router import health_bp
from routers.app_router import app_bp
app = Flask(__name__)

# Register the router (Blueprint)
app.register_blueprint(health_bp)
app.register_blueprint(app_bp)
