from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired('The subject is a required entry.')])
    content = TextAreaField('Content', validators=[DataRequired('The content is a required entry.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired('The content is a required entry.')])