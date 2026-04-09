from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("airports.json") as file:
    airports = json.load(file)

@app.route("/airport/<icao>")
def airport(icao):
    airport = airports.get(icao.upper())
    if airport:
        return jsonify({"icao": icao.upper(),"name": airport["name"],"city": airport["city"],"country": airport["country"]})
    else:
        return jsonify({"error": "unexisting airport"}), 404
if __name__ == "__main__":
    app.run(debug=True, port=5000)