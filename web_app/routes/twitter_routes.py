from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import User, Tweet, db, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users")
def list_users_human_friendly():
    db_users = User.query.all()
    return render_template("users.html", users=db_users, message="List of users contained in the database:")

@twitter_routes.route("/users.json")
def list_users():
    db_users = User.query.all()
    users_response = parse_records(db_users)
    return jsonify(users_response)