from flask_app.controllers import dojos, ninjas
from flask_app import app


# from flask import render_template, request, redirect
# # import the class from user.py
# from user import User

# from flask_app import app

# @app.route("/")
# def index():
#     # call the get all classmethod to get all users
#     users = User.get_all()
#     print(users)
#     return render_template("index.html", users = users)

# @app.route("/users/new")
# def new_user():
#     return render_template ("new.html")    

# @app.route("/create/users", methods=["POST"])
# def create_user():
#     # print(request.form)
#     User.save(request.form)
#     return redirect('/')

# @app.route("/users/<int:id>")
# def show_user(id):
#     data = {"id": id}
#     # User.get_one(data)
#     user = User.get_one(data)
#     return render_template("show.html", user=user)

# @app.route("/users/edit/<int:id>")
# def edit_user(id):
#     data = {"id": id}
#     user = User.get_one(data)
#     return render_template("edit.html", user=user)
            
# @app.route("/users/update", methods=["POST"])
# def update_user():
#     print(request.form)
#     User.update(request.form)
#     return redirect('/')

# @app.route("/users/delete/<int:id>")
# def delete_user(id):
#     data = {"id": id}
#     User.delete(data)
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)