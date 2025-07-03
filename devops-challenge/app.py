from flask import Flask
from routers.health_router import health_bp

app = Flask(__name__)

# Register the router (Blueprint)
app.register_blueprint(health_bp)
