from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Genera una clave secreta aleatoria

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectopeti'

def get_db_connection():
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.before_request
def before_request():
    print("Antes de la petición..")

@app.after_request
def after_request(response):
    print("Después de la petición..")
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['email']
        password = request.form['password']
        
        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM usuario WHERE Correo = %s", (correo,))
            user = cur.fetchone()
        
        connection.close()
        
        if user and check_password_hash(user['Contrasenia'], password):
            session['user'] = user['Correo']
            session['user_id'] = user['IdUsuario']  # Agrega el ID de usuario a la sesión
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('login'))
    
    data = {
        'titulo': 'Iniciar Sesión',
        'Correo': 'Correo electrónico',
        'Password': 'Contraseña'
    }
    return render_template('login/index.html', data=data)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombre = request.form['name']
        apellidos = request.form['surname']
        correo = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        
        if password != password2:
            return redirect(url_for('registrarse'))

        hashed_password = generate_password_hash(password)
        
        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute("INSERT INTO usuario (Nombres, Apellidos, Correo, Contrasenia) VALUES (%s, %s, %s, %s)",
                        (nombre, apellidos, correo, hashed_password))
            connection.commit()
        
        connection.close()
        
        return redirect(url_for('login'))
    
    data = {
        'titulo': 'Regístrate',
        'Nombre': 'Nombre',
        'Apellidos': 'Apellidos',
        'Correo': 'Correo electrónico',
        'Password': 'Contraseña',
        'PasswordRepeat': 'Repite la Contraseña'
    }
    return render_template('login/register.html', data=data)

@app.route('/inicio')
def inicio():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/inicio.html')

@app.route('/csv')
def subir_csv():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/subir-csv.html')

@app.route('/exportar')
def exportar():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/exportar.html')

@app.route('/ajustes')
def ajustes():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/ajustes.html')

@app.route('/crear-plan', methods=['GET', 'POST'])
def crearplan():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nombre_empresa = request.form['nombre_empresa']
        mision = request.form['mision']
        vision = request.form['vision']
        valores1 = request.form['valores1']
        valores2 = request.form['valores2']
        valores3 = request.form['valores3']
        valores4 = request.form['valores4']
        valores5 = request.form['valores5']
        valores6 = request.form['valores6']
        
        connection = get_db_connection()
        with connection.cursor() as cur:
            # Insertar en la tabla valores
            cur.execute("INSERT INTO valores (Valor1, Valor2, Valor3, Valor4, Valor5, Valor6) VALUES (%s, %s, %s, %s, %s, %s)",
                        (valores1, valores2, valores3, valores4, valores5, valores6))
            valores_id = cur.lastrowid  # Obtener el ID de los valores insertados
            
            # Insertar en la tabla empresa
            cur.execute("INSERT INTO empresa (FkUsuario, NombreEmpresa, Mision, Vision, FkValores) VALUES (%s, %s, %s, %s, %s)",
                        (session['user_id'], nombre_empresa, mision, vision, valores_id))
            connection.commit()
        
        connection.close()
        
        return redirect(url_for('inicio'))
    
    return render_template('vistas/crear-plan.html')  # Actualiza la ruta aquí

@app.route('/crear-unidad-estrategica')
def crearunidadestrategica():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/crear-unidad-estrategica.html')

@app.route('/crear-cadena-valor')
def crearcadenavalor():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/body/crear-cadena-valor.html')

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    if 'user' not in session:
        return redirect(url_for('login'))
    data = {
        'nombre': nombre,
        'apellido': 'Chambilla',
        'edad': edad
    }
    return render_template('contacto.html', data=data)

@app.route('/query_string')
def query_string():
    if 'user' not in session:
        return redirect(url_for('login'))
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"

def pagina_no_encontrada(error):
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
