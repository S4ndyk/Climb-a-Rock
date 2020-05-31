from flask import render_template, request, redirect, url_for
from application import app, db
from application.routes.models import Route
from application.routes.forms import RouteForm, UpdateRouteForm
from flask_login import login_required


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/routes", methods=["GET"])
def routes_index():
    return render_template("routes/table.html", routes = Route.query.all())

@app.route("/routes/new")
@login_required
def routes_form():
  return render_template("routes/new.html", form = RouteForm())


@app.route("/routes", methods=["POST"])
@login_required
def routes_create():
  form = RouteForm(request.form)
  new_route = Route(form.name.data, form.route_type.data)
  db.session().add(new_route)
  db.session().commit()
  return redirect(url_for("routes_index"))

@app.route("/routes/<route_id>", methods=["GET"])
@login_required
def routes_update(route_id):
  return render_template("routes/update.html", form = UpdateRouteForm(), id = route_id)

@app.route("/routes/<route_id>", methods=["POST"])
@login_required
def routes_commit(route_id):
  form = UpdateRouteForm(request.form)
  route_to_update = Route.query.get(route_id)
  route_to_update.name = form.new_name.data
  print(route_to_update)
  db.session().commit()
  return redirect(url_for("routes_index"))
