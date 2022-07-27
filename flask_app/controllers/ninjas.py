from flask import render_template, request, redirect
# import the class from ninja.py
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    # call the get all classmethod to get all ninjas
    print(ninjas)
    return render_template("index.html", ninjas = ninjas)

@app.route("/ninjas/new")
def new_ninja():
    dojos = Dojo.get_all()
    return render_template ("new.html", dojos = dojos)    

@app.route("/create/ninjas", methods=["POST"])
def create_ninja():
    # print(request.form)
    Ninja.save(request.form)
    return redirect('/')

@app.route("/ninjas/<int:id>")
def show_ninja(id):
    data = {"id": id}
    # Ninja.get_one(data)
    ninja = Ninja.get_one(data)
    return render_template("show.html", ninja=ninja)

@app.route("/ninjas/edit/<int:id>")
def edit_ninja(id):
    data = {"id": id}
    ninja = Ninja.get_one(data)
    return render_template("edit.html", ninja=ninja)
            
@app.route("/ninjas/update", methods=["POST"])
def update_ninja():
    print(request.form)
    Ninja.update(request.form)
    return redirect('/')

@app.route("/ninjas/delete/<int:id>")
def delete_ninja(id):
    data = {"id": id}
    Ninja.delete(data)
    return redirect('/')

    