from flask import Flask, redirect, url_for, render_template, request
# database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/registro.db"
db = SQLAlchemy(app)


class registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    direccion = db.Column(db.String(200))
    email = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    cedula = db.Column(db.String(200))
    fechadenacimiento = db.Column(db.String(200))
    ciudad = db.Column(db.String(200))
    genero = db.Column(db.String(200))
    contraseña = db.Column(db.String(200))
    confircontra = db.Column(db.String(200))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('PaginaPrincipal/index.html')
    return render_template('PaginaPrincipal/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Login/inicio.html')
    return render_template('Login/inicio.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Registro/registro.html')
    return render_template('Registro/registro.html')


@app.route('/dashboard/Usuarios', methods=['GET', 'POST'])
def DashboardUser():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardOne.html')
    return render_template('Dashboard/dashboardOne.html')


@app.route('/dashboard/Peliculas', methods=['GET', 'POST'])
def DashboardMovie():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardTwo.html')
    return render_template('Dashboard/dashboardTwo.html')


@app.route('/dashboard/Perfil', methods=['GET', 'POST'])
def Dashboard():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardThree.html')
    return render_template('Dashboard/dashboardThree.html')


@app.route('/Perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Perfil/perfil.html')
    return render_template('Perfil/perfil.html')


@app.route('/Funcion', methods=['GET', 'POST'])
def funcion():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Funcion/funcion.html')
    return render_template('Funcion/funcion.html')


@app.route('/Funcion/Ralph', methods=['GET', 'POST'])
def funcion2():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Funcion/funcion2.html')
    return render_template('Funcion/funcion2.html')


@app.route('/Funcion/Avenger', methods=['GET', 'POST'])
def funcion3():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('Funcion/funcion3.html')
    return render_template('Funcion/funcion3.html')


@app.route('/crear-registro', methods=['POST'])
def crear():
    data = registro(nombre=request.form['nombre'], direccion=request.form['direccion'], email=request.form['email'], telefono=request.form['telefono'],
        cedula=request.form['cedula'], fechadenacimiento=request.form['fechadenacimiento'], ciudad=request.form['ciudad'], genero=request.form['genero'],
        contraseña=request.form['contraseña'], confircontra=request.form['confircontra'] )
    db.session.add(data)
    db.session.commit()
    return "saved"


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
