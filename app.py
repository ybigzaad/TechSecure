from config import *
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = db.cursor()

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/ajout", methods=["GET", "POST"])
def ajout():

    if request.method == "POST":

        ville = request.form.get("ville")
        adresse = request.form.get("adresse")
        responsable = request.form.get("responsable")
        employes = request.form.get("employes")
        ip_routeur = request.form.get("ip_routeur")

        if not ville or not adresse or not responsable or not employes or not ip_routeur:
            return "Tous les champs sont obligatoires."

        cursor.execute(
            """
            INSERT INTO filiales
            (ville, adresse, responsable, employes, ip_routeur)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (ville, adresse, responsable, employes, ip_routeur)
        )

        db.commit()

        return "La filiale a été enregistrée avec succès."

    return render_template("ajout_filiale.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/filiales")
def filiales():
    return render_template("filiales.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/entreprise")
def entreprise():
    return render_template("entreprise.html")

if __name__ == "__main__":
    app.run(debug=True)