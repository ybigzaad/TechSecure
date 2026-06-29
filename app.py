from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/filiales")
def filiales():
    return render_template("filiales.html")

@app.route("/ajout")
def ajout():
    return render_template("ajout_filiale.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/entreprise")
def entreprise():
    return render_template("entreprise.html")

if __name__ == "__main__":
    app.run(debug=True)