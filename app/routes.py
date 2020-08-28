from app import app, bcrypt, db
from flask import render_template, url_for, redirect, flash 
from app.forms import LoginForm, SignupForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        flash('The account is created successfully')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('The user is not successfully logged in')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))