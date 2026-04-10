from flask import Flask, render_template, request, redirect, url_for
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Подключение БД
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@127.0.0.1:5432/dsa_lab_4'

db = SQLAlchemy(app)

# Инициализаця flask-login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Модель для работы с пользователями
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Получение данных о пользователе
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Корневая страница
@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect(url_for("login"))

# Страница входа
@app.route("/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    else:
        return render_template("login.html")

# Авторизация
@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return render_template(
            "login.html",
            error="Пользователь с таким email не найден"
        )

    if not user.check_password(password):
        return render_template(
            "login.html",
            error="Неверный пароль"
        )

    login_user(user)
    return redirect(url_for("index"))

# Страница регистрации
@app.route("/signup", methods=["GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    else:
        return render_template("signup.html")

# Регистрация
@app.route("/signup", methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    check_user = User.query.filter_by(email=email).first()

    if check_user:
        return render_template(
            "signup.html",
            error="Пользователь с таким email уже существует"
        )

    new_user = User(name=name, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("login"))

# Выход
@app.route("/logout", methods=["GET"])
def logout():
    if current_user.is_authenticated:
        logout_user()
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
