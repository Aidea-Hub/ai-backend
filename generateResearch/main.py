from flask import jsonify


def generateSearch(request):
    return jsonify({"result": "Search Result"}), 200
