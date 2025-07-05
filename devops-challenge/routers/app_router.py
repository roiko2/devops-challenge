from flask import Blueprint, jsonify
import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, TABLE_NAME

app_bp = Blueprint('app', __name__)

@app_bp.route('/secret', methods=['GET'])
def get_secret_code(secret_code='theDoctor'):
    session = boto3.Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_REGION
    )
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'codeName': f'{secret_code}'})

    return jsonify({
        'secret_code': f'{response.get("Item")["secretCode"]}'
    })