from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


def test_function():
    l = []
    for i in range(10):
        l.append(i)

    return l


if __name__ == "__main__":
    app.run(debug=True)
