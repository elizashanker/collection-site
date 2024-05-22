from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, MultipleFileField, SubmitField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):
    title = StringField("Название")
    author_id = IntegerField('Айди автора')
    creation_year = IntegerField('Год создания')
    creation_history = TextAreaField("История создания")
    creation_place = StringField("Место создания")
    collection_history = TextAreaField("История попадания в коллекцию")
    materials = StringField("Материалы")
    photos = MultipleFileField("Фото")
    series_id = IntegerField('Айди автора')

    submit = SubmitField('Добавить')