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
            session['user_id'] = user['IdUsuario']
            session['user_name'] = user['Nombres']
            session['user_surname'] = user['Apellidos']
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
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_surname', None)
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
    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM empresa WHERE FkUsuario = %s", (session['user_id'],))
        empresas = cur.fetchall()
    
    connection.close()

    user_data = {
        'Nombres': session['user_name'],
        'Apellidos': session['user_surname']
    }

    return render_template('vistas/body/inicio.html', empresas=empresas, user_data=user_data)

@app.route('/crear-plan', methods=['GET', 'POST'])
def crearplan():
    if 'user_id' not in session:
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
            cur.execute("INSERT INTO valores (Valor1, Valor2, Valor3, Valor4, Valor5, Valor6) VALUES (%s, %s, %s, %s, %s, %s)",
                        (valores1, valores2, valores3, valores4, valores5, valores6))
            valores_id = cur.lastrowid
            connection.commit()

        with connection.cursor() as cur:
            cur.execute("INSERT INTO empresa (FkUsuario, NombreEmpresa, Mision, Vision, FkValores) VALUES (%s, %s, %s, %s, %s)",
                        (session['user_id'], nombre_empresa, mision, vision, valores_id))
            empresa_id = cur.lastrowid
            connection.commit()
        
        connection.close()
        
        session['empresa_id'] = empresa_id  # Guardar el ID de la empresa en la sesión para usarlo después
        session['mision'] = mision  # Guardar la misión en la sesión para usarla después
        
        return redirect(url_for('crearunidadestrategica'))
    
    return render_template('vistas/crear-plan.html')

@app.route('/crear-unidad-estrategica', methods=['GET', 'POST'])
def crearunidadestrategica():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        empresa_id = session.get('empresa_id')
        mision = session.get('mision')
        
        obj_gen1 = request.form['obj_gen1']
        obj_gen2 = request.form['obj_gen2']
        obj_gen3 = request.form['obj_gen3']
        obj_esp1_1 = request.form['obj_esp1_1']
        obj_esp1_2 = request.form['obj_esp1_2']
        obj_esp1_3 = request.form['obj_esp1_3']
        obj_esp2_1 = request.form['obj_esp2_1']
        obj_esp2_2 = request.form['obj_esp2_2']
        obj_esp2_3 = request.form['obj_esp2_3']
        obj_esp3_1 = request.form['obj_esp3_1']
        obj_esp3_2 = request.form['obj_esp3_2']
        obj_esp3_3 = request.form['obj_esp3_3']
        
        connection = get_db_connection()
        with connection.cursor() as cur:
            # Insertar en la tabla objetivosestrategicos
            cur.execute("INSERT INTO objetivosestrategicos (FkEmpresa) VALUES (%s)", (empresa_id,))
            objetivos_est_id = cur.lastrowid
            connection.commit()

            # Insertar en la tabla objetivosgenerales
            cur.execute("INSERT INTO objetivosgenerales (FkObjetivosEst, ObjGeneral1, ObjGeneral2, ObjGeneral3) VALUES (%s, %s, %s, %s)",
                        (objetivos_est_id, obj_gen1, obj_gen2, obj_gen3))
            obj_gen_id = cur.lastrowid
            connection.commit()

            # Insertar en la tabla objetivosespecificos
            cur.execute("INSERT INTO objetivosespecificos (FkObjetivosGen, ObjEspecifico1, ObjEspecifico2, ObjEspecifico3) VALUES (%s, %s, %s, %s)",
                        (obj_gen_id, obj_esp1_1, obj_esp1_2, obj_esp1_3))
            cur.execute("INSERT INTO objetivosespecificos (FkObjetivosGen, ObjEspecifico1, ObjEspecifico2, ObjEspecifico3) VALUES (%s, %s, %s, %s)",
                        (obj_gen_id, obj_esp2_1, obj_esp2_2, obj_esp2_3))
            cur.execute("INSERT INTO objetivosespecificos (FkObjetivosGen, ObjEspecifico1, ObjEspecifico2, ObjEspecifico3) VALUES (%s, %s, %s, %s)",
                        (obj_gen_id, obj_esp3_1, obj_esp3_2, obj_esp3_3))
            connection.commit()
        
        connection.close()
        
        return redirect(url_for('crearcadenavalor'))
    
    mision = session.get('mision', '')  # Obtener la misión de la sesión
    
    return render_template('vistas/crear-unidad-estrategica.html', mision=mision)

@app.route('/crear-cadena-valor', methods=['GET', 'POST'])
def crear_cadena_valor():
    if request.method == 'POST':
        empresa_id = session.get('empresa_id')
        respuestas = []
        for i in range(1, 15):
            respuestas.append(int(request.form.get(f'respuesta{i}', 0)))
        fortalezas = [request.form[key] for key in request.form if key.startswith('fortaleza')]
        debilidades = [request.form[key] for key in request.form if key.startswith('debilidad')]

        resultado = 1 - sum(respuestas) / 100

        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute("INSERT INTO cuestionario (FkEmpresa, Resultado) VALUES (%s, %s)", (empresa_id, resultado))
            cuestionario_id = cur.lastrowid
            for i, respuesta in enumerate(respuestas):
                cur.execute("INSERT INTO respuestas (FkCuestionario, Pregunta, Respuesta) VALUES (%s, %s, %s)",
                            (cuestionario_id, f'Pregunta {i+1}', respuesta))
            for fortaleza in fortalezas:
                cur.execute("INSERT INTO fortalezas (FkCuestionario, Fortaleza) VALUES (%s, %s)", (cuestionario_id, fortaleza))
            for debilidad in debilidades:
                cur.execute("INSERT INTO debilidades (FkCuestionario, Debilidad) VALUES (%s, %s)", (cuestionario_id, debilidad))
            connection.commit()
        connection.close()

        return redirect(url_for('resultado_cuestionario', cuestionario_id=cuestionario_id))

    preguntas = [
        "A. La empresa no tiene deficiencia alguna de los defectos en la producción de productos/servicios.",
        "B. La empresa omite los medios productivos tecnológicos eficientemente.",
        "D. La evaluación y dispersión de los sistemas de información y control de gestión definida y eficaz.",
        "E. Los mercados técnicos y tecnológicos de la empresa están implantados para competir en un futuro a corto, medio y largo plazo.",
        "F. La empresa no tiene ningún problema de organización.",
        "G. La empresa es un referente en su sector en I+D+I.",
        "H. La ascendencia de los procedimientos de la empresa (en ISO, etc.) le da una ventaja competitiva.",
        "I. La empresa dispone de páginas web, y esto se emplea para mantener relaciones con clientes y proveedores.",
        "J. Existe una política de promoción exterior coherente.",
        "K. Los productos/servicios que desarrolla nuestra empresa tienen una tecnología difícil de imitar.",
        "L. La empresa es referente en su sector en la optimización, en términos de coste, de su cadena de producción.",
        "M. La informatización de la empresa es una fuente de ventaja competitiva respecto a sus competidores.",
        "N. Los canales de distribución de la empresa son una correcta logística y valorados por el cliente respecto a nuestros competidores."
    ]
    return render_template('vistas/crear-cadena-valor.html', preguntas=preguntas)

@app.route('/resultado-cuestionario/<int:cuestionario_id>')
def resultado_cuestionario(cuestionario_id):
    connection = get_db_connection()
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM cuestionario WHERE IdCuestionario = %s", (cuestionario_id,))
        cuestionario = cur.fetchone()
        cur.execute("SELECT * FROM respuestas WHERE FkCuestionario = %s", (cuestionario_id,))
        respuestas = cur.fetchall()
        cur.execute("SELECT * FROM fortalezas WHERE FkCuestionario = %s", (cuestionario_id,))
        fortalezas = cur.fetchall()
        cur.execute("SELECT * FROM debilidades WHERE FkCuestionario = %s", (cuestionario_id,))
        debilidades = cur.fetchall()
    connection.close()
    return render_template('vistas/resultado.html', cuestionario=cuestionario, respuestas=respuestas, fortalezas=fortalezas, debilidades=debilidades)

@app.route('/csv')
def subir_csv():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/subir-csv.html')

@app.route('/exportar')
def exportar():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/exportar.html')

@app.route('/ajustes')
def ajustes():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('vistas/ajustes.html')

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    data = {
        'nombre': nombre,
        'apellido': 'Chambilla',
        'edad': edad
    }
    return render_template('contacto.html', data=data)

@app.route('/query_string')
def query_string():
    if 'user_id' not in session:
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
