from flask import Flask, request, jsonify
from flask_cors import CORS
from generate_message import generate_message

app = Flask(__name__)
CORS(app)


@app.route("/api/generate-response", methods=["POST"])
def generate_response():
    try:
        data = request.json
        query = data['query']
        past_messages = data['pastMessages']
        generated_response = generate_message(query, past_messages)
        source_documents = []
        for doc in generated_response['source_documents']:
            source_documents.append(
                {'page_content': doc.page_content, 'metadata': doc.metadata})
        response = {
            'result': generated_response['answer'], 'source_documents': source_documents}
        return jsonify(response), 200
    except Exception as e:
        print('An error occurred:', e, flush=True)


@app.route("/api/healthcheck", methods=["GET"])
def health_check():
    return {'status': 'success', 'message': 'Flask integrated with Next!'}
