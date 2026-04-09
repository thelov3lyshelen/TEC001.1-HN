from flask import Flask, jsonify
app = Flask(__name__)
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return True
@app.route("/prime_number/<int:number>")
def prime_number(number):
    result = prime(number)
    response = {"number": number,"isPrime": result}
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
# the program will start a test server, google "http://127.0.0.1:5000/prime_number/(prime number here)" after run to continue