from flask import Flask, request, jsonify
from generate_message import generate_message

app = Flask(__name__)


@app.route("/api/generate-response", methods=["POST"])
def generate_response():
    data = request.json
    print(data)
    query = data['query']
    print(query)
    system_message = generate_message(query)
    response = {"data": system_message}
    return response, 200


@app.route("/api/healthcheck", methods=["GET"])
def health_check():
    return {'status': 'success', 'message': 'Flask integrated with Next!'}
