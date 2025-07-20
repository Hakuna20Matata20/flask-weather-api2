from flask import Flask, request, jsonify
import awsgi

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "Unknown")
    return jsonify({
        "city": city,
        "temperature": f"{20 + hash(city) % 15}°C",
        "condition": "Sunny"
    })

def lambda_handler(event, context):
    # AWS Lambda entry point — обов’язково поза if __name__ == "__main__"
    return awsgi.response(app, event, context)

if __name__ == "__main__":
    # Локальний запуск для тесту
    app.run(debug=True, port=3000)
