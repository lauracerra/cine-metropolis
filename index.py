from flask import Flask,redirect,url_for,render_template,request
# database
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
# from flask import g

# DATABASE = '/datebase/metropolis.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
# # database

app=Flask(__name__)     
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datebase/metropolis.db"      
login_manager = LoginManager(app)       
login_manager.login_view = "login"      
db = SQLAlchemy(app)    




@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('PaginaPrincipal/index.html')
    return render_template('PaginaPrincipal/index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Login/inicio.html')
    return render_template('Login/inicio.html')


@app.route('/registro',methods=['GET','POST'])
def registro():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Registro/registro.html')
    return render_template('Registro/registro.html')

@app.route('/dashboard/Usuarios',methods=['GET','POST'])
def DashboardUser():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardOne.html')
    return render_template('Dashboard/dashboardOne.html')

@app.route('/dashboard/Peliculas',methods=['GET','POST'])
def DashboardMovie():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardTwo.html')
    return render_template('Dashboard/dashboardTwo.html')

@app.route('/dashboard/Perfil',methods=['GET','POST'])
def Dashboard():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Dashboard/dashboardThree.html')
    return render_template('Dashboard/dashboardThree.html')

@app.route('/Perfil',methods=['GET','POST'])
def perfil():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Perfil/perfil.html')
    return render_template('Perfil/perfil.html')

@app.route('/Funcion',methods=['GET','POST'])
def funcion():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('Funcion/funcion.html')
    return render_template('Funcion/funcion.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)