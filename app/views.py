from flask import request, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
from .utils import simulate_network_latency


@app.route("/user/create", methods=["GET"])
def user_records():
    """Create a user via query string parameters."""
    username = request.args.get("user")
    if username:
        new_user = User(
            username=username,
            created=dt.now(),
            admin=False,
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize())
    return jsonify({"error": "Missing 'user' field"}), 400


@app.route("/users/list", methods=["GET"])
@simulate_network_latency
def users_get():
    users = db.session.query(User).all()
    return jsonify([user.serialize() for user in users])


@app.route("/user/details", methods=["GET"])
@simulate_network_latency
def user_get_by_id():
    user_id = request.args.get("id")
    results_proxy = db.engine.execute(f"select * from users where (id = '{user_id}')")
    results = [{**row} for row in results_proxy]
    return jsonify(results)


@app.route("/user/exists", methods=["GET"])
@simulate_network_latency
def user_exists_by_id():
    user_id = request.args.get("id")
    results_proxy = db.engine.execute(
        f"select * from users where id = '{user_id}' limit 1"
    )
    user_exists = bool(len(list(results_proxy)))
    return jsonify({"user_exists": user_exists})


@app.route("/user/blind", methods=["GET"])
@simulate_network_latency
def users_blind_query():
    user_id = request.args.get("id")
    db.engine.execute(f"select * from users where id = '{user_id}' limit 1")
    return jsonify({"msg": "Response does not include results from database"})


@app.route("/users/create", methods=["GET"])
def users_create():
    users = ["admin", "bobo", "tomtom"]

    for user in users:
        try:
            new_user = User(
                username=user,
                created=dt.now(),
                admin=False
            )
            db.session.add(new_user)
            db.session.commit()
        except Exception:
            pass
    return users_get()
