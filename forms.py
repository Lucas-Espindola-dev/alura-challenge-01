from wtforms import StringField, SubmitField, Form
from wtforms.validators import DataRequired


class SearchForm(Form):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('search',
                         render_kw={'class': 'btn btn-sucess btn-block'})
