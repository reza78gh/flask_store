from flask import Blueprint ,request,render_template , url_for,current_app
import json
from flask import redirect
from cryptography.fernet import Fernet

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"] 
        with open("flask_store/users.json") as user_file:
            users = json.load(user_file)
            cipher_suite = Fernet(current_app.config['CIPHER_KEY'])
            for user in users:
                unciphered_pass = (cipher_suite.decrypt(bytes(user[1],'utf-8'))).decode("utf-8")
                if username == user[0] and password == unciphered_pass:
                    return redirect(url_for("hello"))
            return render_template("login.html",error="incorect user or pass")
    else:
        return render_template("login.html",error="")