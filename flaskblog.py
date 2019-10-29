from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2b471c51fd96d28fa3ec'

posts = [
    {
        'author':'Ishmael Nkurumwa',
        'title': 'First post content',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
 
@app.route("/about")
def about():
    return render_template('about.html', title='About ')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # db.session.add(user)
        # db.session.commit()
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'nkurumwa51@gmail.com' and form.password.data == 'password':
            flash('Logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect details. Kindly ensure you input correct details', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)