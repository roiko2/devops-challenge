from flask import Blueprint, jsonify
from config import IMAGE_REPOSITORY, GITHUB_REPOSITORY


health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'container': f'{IMAGE_REPOSITORY}',
        'project': f'{GITHUB_REPOSITORY}'
    })
