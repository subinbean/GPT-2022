from flask import Flask

app = Flask(__name__)


@app.route("/api/healthcheck", methods=["GET"])
def healthCheck():
    return {'status': 'success', 'message': 'Flask integrated with Next!'}
