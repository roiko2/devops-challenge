from flask import Blueprint, jsonify
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY_ID

app_bp = Blueprint('app', __name__)

@app_bp.route('/secret', methods=['GET'])
def health_check():
    return jsonify({
        'secret_code': 'test'
    })