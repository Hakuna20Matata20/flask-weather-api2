from flask import Flask, request, jsonify
from aws_lambda_wsgi import response

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "Unknown")
    return jsonify({"city": city, "temperature": "25°C", "condition": "Sunny"})

def lambda_handler(event, context):
    # Це точка входу для AWS Lambda
    return response(app, event, context)

if __name__ == "__main__":
    # Для локального тесту
    app.run(debug=True, port=3000)
