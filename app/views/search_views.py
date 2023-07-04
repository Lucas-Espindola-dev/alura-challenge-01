from forms import SearchForm
from app import app
from flask import redirect, url_for


@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchForm
    if not form.validate_on_submit():
        return redirect(url_for('index'))
