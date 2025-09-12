from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def two_hundred():
    return "<h2>200! all is good with URI</h2>"

@app.route("/error")
def error():
    abort(500, "Oops!!! There is some error!")

if __name__ == "__main__":
    app.run(debug=True, port=000, host="0.0.0.0")


