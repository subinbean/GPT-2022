from flask import Flask, request, jsonify
from flask_cors import CORS
from generate_message import generate_message

app = Flask(__name__)
CORS(app)


@app.route("/api/generate-response", methods=["POST"])
def generate_response():
    try:
        data = request.json
        print(request)
        print(data)
        query = data['query']
        system_message = generate_message(query)
        response = {"data": system_message}
        return response, 200
    except Exception as e:
        print('An error occurred:', e)


@app.route("/api/healthcheck", methods=["GET"])
def health_check():
    return {'status': 'success', 'message': 'Flask integrated with Next!'}
