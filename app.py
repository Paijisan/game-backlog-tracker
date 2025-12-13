from flask import Flask, request , render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_game():
    title = request.form.get["title"]
    platform = request.form.get["platform"]
    status = request.form.get["status"]

    return f"Received: {title}, {platform}, {status}"

if __name__ == "__main__":
    app.run(debug=True)
    