from flask import Flask, render_template

app = Flask(__name__)

PASSWORD_INPUT = "ginger"

PASSWORD = "ginger"


@app.route("/")
def home():

    unlocked = PASSWORD_INPUT == PASSWORD

    return render_template(
        "index.html",
        unlocked=unlocked
    )


@app.route("/page1")
def page1():
    return render_template("page1.html")


@app.route("/page2")
def page2():
    return render_template("page2.html")


@app.route("/page3")
def page3():
    return render_template("page3.html")


@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)