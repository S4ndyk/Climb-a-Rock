from flask import render_template, request, redirect, url_for
from application import app, db
from application.ascents.forms import AscentForm
from application.ascents.models import Ascent


@app.route('/send', methods=['POST'])
def ascent_create():
  if request.method == "GET":
    return render_template("routes/table.html")
  form = AscentForm(request.form)
  ascent = Ascent(form.grade.data, form.route_id.data, form.user_id.data)
  db.session().add(ascent)
  db.session().commit()
  return redirect(url_for("routes_index"))