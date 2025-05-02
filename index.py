from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    context = {
        "menus": [
            "Home",
            "About",
            "Contact",
            "Shop",
            "Blog",
            "Films",
            "Videos",
        ],
    }
    return render_template("index.html", **context)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
