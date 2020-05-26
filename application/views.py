from flask import render_template, request, redirect, url_for
from application import app, db
from application.routes.models import Route


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/routes", methods=["GET"])
def routes_index():
    return render_template("routes/table.html", routes = Route.query.all())

@app.route("/routes/new")
def routes_form():
  return render_template("routes/new.html")


@app.route("/routes", methods=["POST"])
def routes_create():
  route_name = request.form.get("name")
  route_type = request.form.get("routetype")
  new_route = Route(route_name, route_type)
  db.session().add(new_route)
  db.session().commit()
  return redirect(url_for("routes_index"))
