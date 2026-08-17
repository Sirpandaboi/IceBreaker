from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CORRECT_CODE = """Enter the password in the correct order throughout the website to unlock the resources. The password is hidden in (ALMOST) plain sight.

I.      = app.
II.     = run
III.    = (Debug=
IV.     = True)"""

LINK_1 = "https://www.canva.com/design/DAHR7okqzn8/-CjH4uSSssX8uPfWSWwFPg/edit"
LINK_2 = "https://example.com/link2"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cloud")
def cloud():
    return render_template("cloud.html")

@app.route("/run", methods=["POST"])
def run_code():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "output": [
                "ERROR: No source code received."
            ]
        })

    code = data.get("code", "")

    if code == CORRECT_CODE:

        return jsonify({
            "success": True,

            "output": [
                "Compiling source...",
                "Compilation successful.",
                "",
                "Process finished with exit code 0.",
                "",
                "Two resources have been unlocked."
            ],

            "links": [
                {
                    "name": "Reward 1: Canva Link",
                    "url": LINK_1
                },
                {
                    "name": "Reward 2: Website Source Code",
                    "url": LINK_2
                }
            ]
        })

    else:

        return jsonify({
            "success": False,

            "output": [
                "Compiling source...",
                "",
                "ERROR: Compilation failed.",
                "SyntaxError: unexpected token",
                "at line 1, column 1",
                "",
                "Process finished with exit code 1."
            ]
        })

if __name__ == "__main__":
    app.run(debug=True)