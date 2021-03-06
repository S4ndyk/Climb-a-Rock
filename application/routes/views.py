from flask import render_template, request, redirect, url_for
from application import app, db
from application.routes.models import Route
from application.routes.forms import RouteForm, UpdateRouteForm
from application.ascents.forms import AscentForm
from flask_login import login_required, current_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/routes/all/", methods=["GET"])
def routes_index():
    return render_template("routes/list.html", routes = Route.query.all())

@app.route("/routes/new/")
@login_required
def routes_form():
  return render_template("routes/new.html", form = RouteForm())

@app.route("/routes/", methods=["POST"])
@login_required
def routes_create():
  form = RouteForm(request.form)
  new_route = Route(form.name.data, form.route_type.data)
  db.session().add(new_route)
  db.session().commit()
  return redirect(url_for("routes_index"))

@app.route("/routes/<route_id>", methods=["GET"])
@login_required
def routes_view(route_id):
  route = Route.query.get(route_id)
  return render_template("routes/route.html", route = route, form = AscentForm(route_id = route_id, user_id = current_user.id))

@app.route("/routes/edit/<route_id>", methods=["GET"])
@login_required
def routes_update(route_id):
  route = Route.query.get(route_id)
  return render_template("routes/update.html", route = route, form = UpdateRouteForm())

@app.route("/routes/<route_id>", methods=["POST"])
@login_required
def routes_commit(route_id):
  form = UpdateRouteForm(request.form)
  route_to_update = Route.query.get(route_id)
  route_to_update.name = form.new_name.data
  db.session().commit()
  return redirect(url_for("routes_index"))
