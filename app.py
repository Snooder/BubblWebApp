import os
from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy #TODO: possibly for db stuff?
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#basic config for app to work/run
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
bootstrap = Bootstrap(app)

#oop class for register form form wtforms
class RegisterForm(FlaskForm):
    email = StringField("Email Address", validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])

#home page for now
@app.route('/', methods=['GET', 'POST'])
def index():
	#create register form and check if succesfully submitted
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        emails = set() #TODO store in db
        return redirect(url_for('signup_success')) #show success
    else:
        return render_template('index.html', form=form) #not success lol

#rendering for success page
@app.route('/success')
def signup_success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True) #runs on localhost, port 5000 default i believe