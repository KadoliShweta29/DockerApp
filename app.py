from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This is CICD using all CICD tools and AWS @@@@ branch chang"

app.run(host="0.0.0.0", port=5000)
