from flask import render_template,flash,redirect
from app import app
from .forms import loginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'zpc'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Login requested for openid="' + form.openid.data + '",remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form= form,
                           providers = app.config['OPENID_PROVIDERS'])