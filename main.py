from flask import Flask, url_for, render_template, redirect
from data import db_session
from data.admin import AdminForm
from data.users import Object
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '775664a9b6ace72dedb42f592cb19a2789935126497200fc1aee8eb2a12d23b9'

@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        object = Object()
        object.title = form.title.data

        object.author_id = form.author_id.data
        object.creation_year = form.creation_year.data
        object.creation_history = form.creation_history.data
        object.creation_place = form.creation_place.data
        object.collection_history = form.collection_history.data
        object.materials = form.materials.data
        object.photos = ""

        for image in form.photos.data:
            filename = secure_filename(image.filename)
            image.save(os.path.join('static\img', filename))
            object.photos += f";{filename};"
        print(object.photos)

        object.series_id = form.series_id.data
        db_sess.add(object)
        db_sess.commit()
        return redirect("/admin")

    return render_template("admin.html", form=form)


@app.route('/')
def missia():
    return render_template('index.html')


@app.route("/objects")
def deviz():
    db_sess = db_session.create_session()
    objects = db_sess.query(Object).all()
    print(objects)
    return render_template("objects.html", objects=objects)

@app.route("/about<int:id>")
def about_object(id):
    db_sess = db_session.create_session()
    object = db_sess.query(Object).filter(Object.id == id).first()
    print(object)
    return render_template("about_object.html", object=object)


if __name__ == '__main__':
    db_session.global_init("db/users.db")
    app.run(port=5000, host="127.0.0.1", debug=True)
