from flask import Flask, redirect, render_template, request, url_for
from cs50 import SQL
from datetime import datetime
from helpers import *

# app configuration
app = Flask(__name__)

# database configuration
db = SQL("sqlite:///shortUrls.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        data = {
            "fullUrl": request.args.get("fullUrl", ""),
            "shortUrl": request.args.get("shortUrl", ""),
            "message": request.args.get("message", ""),
        }

        return render_template("index.html", data=data)

    fullUrl = request.form.get("url-input")
    shortUrl = request.form.get("custom-input")

    # Invalid Shor URL
    if not shortUrl.isalnum():
        return redirect(
            url_for("index", fullUrl=fullUrl, shortUrl=shortUrl, message="invalid")
        )

    data = db.execute("SELECT shortUrl FROM urlData where shortUrl = ?", shortUrl)

    # Already taken
    if len(data) != 0:
        return redirect(
            url_for("index", fullUrl=fullUrl, shortUrl=shortUrl, message="taken")
        )

    db.execute(
        "INSERT INTO urlData VALUES(?, ?, ?, ?)",
        shortUrl,
        fullUrl,
        0,
        datetime.now(),
    )

    return redirect(
        url_for("index", fullUrl=fullUrl, shortUrl=shortUrl, message="success")
    )


@app.route("/database")
def database():
    data = db.execute("SELECT * FROM urlData ORDER BY lastClicked DESC")

    return render_template("database.html", data=data, time_ago=time_ago)


@app.route("/<short_url>")
def get_short_url(short_url):
    data = db.execute("SELECT * FROM urlData WHERE shortUrl = ?", short_url)

    if len(data) == 0:
        return "<h1>URL Not Found</h1>"

    time_diff = datetime.now() - datetime.strptime(
        data[0]["lastClicked"], "%Y-%m-%d %H:%M:%S"
    )

    if time_diff.seconds > 2:
        db.execute(
            "UPDATE urlData SET clickCount = clickCount + 1, lastClicked = ? WHERE shortUrl = ?",
            datetime.now(),
            short_url,
        )

    return redirect(data[0]["fullUrl"])


if __name__ == "__main__":
    app.run(debug=True)
