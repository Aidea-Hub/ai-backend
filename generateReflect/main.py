from flask import jsonify


def generateReflect(request):
    return jsonify({"result": "Reflect Result"}), 200
