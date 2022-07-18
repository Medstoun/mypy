import os

from flask import Flask, request, Response
from flask_restx import abort
from utils import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query() -> Response:

    cmd_1 = request.args.get('cmd_1')
    val_1 = request.args.get('val_1')
    cmd_2 = request.args.get('cmd_2')
    val_2 = request.args.get('val_2')
    file_name = request.args.get('file_name')

    if not (cmd_1 and val_1 and file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, str(file_name))
    if not os.path.exists(file_path):
        return abort(400)

    with open(file_path) as file:
        res = build_query(str(cmd_1), str(val_1), file)
        if cmd_2 and val_2:
            res = build_query(str(cmd_2), str(val_2), iter(res))

    return app.response_class('\n'.join(res), content_type="text/plain")


if __name__ == '__main__':
    app.run()
