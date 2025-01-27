from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



#example redirects if I have an admin page it takes them back to homepage if they are not logged in. 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/projects")
def projects():
    return render_template("projects.html")






if __name__ == "__main__":
    app.run(debug = True)