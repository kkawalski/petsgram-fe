from flask import redirect, render_template, session, url_for

from auth import auth_blueprint
from auth.forms import LoginForm, RegisterUserForm
from auth.utils import access, create_user, get_current_user


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        auth = access(**form.data)
        auth.store_in_session()
        user = get_current_user()
        user.store_in_session()
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = create_user(**form.data)
        user.store_in_session()
        auth = access(**form.data)
        auth.store_in_session()
        return redirect(url_for("home"))
    return render_template("register.html", form=form)
