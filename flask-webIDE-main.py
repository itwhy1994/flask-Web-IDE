from flask import Flask, render_template, request, Response
import run_code

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/idepy", methods=["GET", "POST"])
def idepy():
    if request.method == "GET":
        return render_template("idepy.html")
    elif request.method == "POST":
        code = request.form["code"]
        res = run_code.main(code)
        resp = Response(str(res))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, False)

