from flask import render_template, request, redirect
# import the class from dojo.py
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route("/")
def dojos():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)

@app.route("/dojos/new")
def new_dojo():
    return render_template ("new.html")    

@app.route("/create/dojos", methods=["POST"])
def create_dojo():
    # print(request.form)
    Dojo.save(request.form)
    return redirect('/')

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {"id": id}
    # Dojo.get_one(data)
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template("show.html", dojo=dojo)

@app.route("/dojos/edit/<int:id>")
def edit_dojo(id):
    data = {"id": id}
    dojo = Dojo.get_one(data)
    return render_template("edit.html", dojo=dojo)
            
@app.route("/dojos/update", methods=["POST"])
def update_dojo():
    print(request.form)
    Dojo.update(request.form)
    return redirect('/')

@app.route("/dojos/delete/<int:id>")
def delete_dojo(id):
    data = {"id": id}
    Dojo.delete(data)
    return redirect('/')

