from flask import render_template, flash, redirect
from app import app
from .forms import InputForm
from os.path import expanduser
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        with open(expanduser('~') + '/messages.txt', 'a') as f:
            f.write('%s %s\n' % (datetime.now(), form.content.data))
        return redirect('/')
    return render_template('index.html',
                           form=form)
