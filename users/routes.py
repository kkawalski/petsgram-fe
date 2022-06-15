from flask import redirect, render_template, url_for

from auth.permissions import login_required, profile_required
from users import users_blueprint
from users.forms import ProfileForm
from users.models import Profile, User
from users.utils import create_profile, get_my_profile, get_profiles, update_my_profile, upload_avatar


@users_blueprint.route("/create", methods=["GET", "POST"])
@login_required
def profile_create():
    user = User.from_session()
    if user.has_profile:
        return redirect(url_for("users.my_profile"))
    form = ProfileForm()
    if form.validate_on_submit():
        profile_data = dict(form.data)
        avatar = profile_data.pop("avatar")
        profile = create_profile(**profile_data)
        avatar = upload_avatar(file=avatar)
        profile.avatar = avatar
        profile.store_in_session()
        user = User.from_session()
        user.has_profile = True
        user.store_in_session()
        return redirect(url_for("home"))
    return render_template("create_profile.html", form=form)


@users_blueprint.route("/me", methods=["GET", "POST"])
@profile_required
def my_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        profile_data = dict(form.data)
        avatar = profile_data.pop("avatar")
        profile = update_my_profile(**profile_data)
        avatar = upload_avatar(file=avatar)
        profile.avatar = avatar
        profile.store_in_session()
    profile = Profile.from_session()
    if profile is None:
        profile = get_my_profile()
        profile.store_in_session()
    form.first_name.data = profile.first_name
    form.last_name.data = profile.last_name
    form.description.data = profile.description
    return render_template("my_profile.html", form=form, profile=profile)


@users_blueprint.route("/", methods=["GET"])
@profile_required
def profile_list():
    profiles = get_profiles()
    print(profiles)
    return render_template("profiles_list.html", profiles=profiles)
