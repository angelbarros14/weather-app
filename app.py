from flask import Flask, request, flash, redirect, render_template

from api import lookup

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name.isdigit() or not name:
            flash("Input a valid city name")
            return redirect("/")
            
        contents = lookup(name)
        if not contents:
            return redirect ("/")
        
        return render_template("index.html", contents=contents)
    
    contents = lookup("Manila")
    return render_template("index.html", contents=contents)