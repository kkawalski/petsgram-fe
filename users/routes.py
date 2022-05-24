from flask import redirect, render_template, url_for
from users import users_blueprint

from users.forms import ProfileForm
from users.models import Profile, User
from users.utils import create_profile, get_my_profile, update_my_profile


@users_blueprint.route("/create", methods=["GET", "POST"])
def profile_create():
    form = ProfileForm()
    if form.validate_on_submit():
        profile = create_profile(**form.data)
        profile.store_in_session()
        user = User.from_session()
        user.has_profile = True
        user.store_in_session()
        return redirect(url_for("home"))
    return render_template("create_profile.html", form=form)


@users_blueprint.route("/me", methods=["GET", "POST"])
def my_profile():
    form = ProfileForm()
    profile = Profile.from_session() or get_my_profile()
    if form.validate_on_submit():
        profile = update_my_profile(**form.data)
        profile.store_in_session()
    return render_template("my_profile.html", form=form, profile=profile)
