from urllib import request
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.method)
        print(20*"=")
        print(request.form)
        print(request.form.get("nama"))
        print(request.form.get("detail"))
        print(20*"=")

    print(request.method)
    
    data = ["apel", "pear", "anggur"]
    return render_template("index.html", contex=data)

if __name__ == "__main__":
    app.run()