from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)  # instancia
app.secret_key = os.urandom(24)  # Genera una clave secreta aleatoria

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'plan_estrategico'

def get_db_connection():
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
def calculate_total(form_data):
    total = 0
    num_preguntas = 25
    max_score = num_preguntas * 4
    
    for i in range(1, num_preguntas + 1):
        respuesta = form_data.get(f'pregunta{i}')
        if respuesta:
            total += int(respuesta)
    
    percentage = ((max_score - total) / max_score) * 100
    return round(percentage, 2)

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
            cur.execute("SELECT * FROM usuarios WHERE correo_electronico = %s", (correo,))
            user = cur.fetchone()
        
        connection.close()
        
        if user and check_password_hash(user['contrasena'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['nombre']
            session['user_surname'] = user['apellidos']
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
            cur.execute("INSERT INTO usuarios (nombre, apellidos, correo_electronico, contrasena) VALUES (%s, %s, %s, %s)",
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
        cur.execute("SELECT * FROM planes_estrategicos WHERE usuario_id = %s", (session['user_id'],))
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

        valores = []
        for i in range(1, 7):
            valor = request.form.get(f'valores{i}')
            if valor:
                valores.append(valor)
            else:
                valores.append(None)

        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute(
                """
                INSERT INTO planes_estrategicos (usuario_id, nombre_empresa, mision, vision) 
                VALUES (%s, %s, %s, %s)
                """, 
                (session['user_id'], nombre_empresa, mision, vision)
            )
            empresa_id = cur.lastrowid

            for valor in valores:
                if valor:
                    cur.execute(
                        "INSERT INTO valores (plan_id, valor) VALUES (%s, %s)",
                        (empresa_id, valor)
                    )

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
            cur.execute(
                "INSERT INTO objetivos_generales (plan_id, objetivo_general) VALUES (%s, %s)",
                (empresa_id, obj_gen1)
            )
            obj_gen1_id = cur.lastrowid

            cur.execute(
                "INSERT INTO objetivos_generales (plan_id, objetivo_general) VALUES (%s, %s)",
                (empresa_id, obj_gen2)
            )
            obj_gen2_id = cur.lastrowid

            cur.execute(
                "INSERT INTO objetivos_generales (plan_id, objetivo_general) VALUES (%s, %s)",
                (empresa_id, obj_gen3)
            )
            obj_gen3_id = cur.lastrowid

            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen1_id, obj_esp1_1)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen1_id, obj_esp1_2)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen1_id, obj_esp1_3)
            )

            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen2_id, obj_esp2_1)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen2_id, obj_esp2_2)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen2_id, obj_esp2_3)
            )

            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen3_id, obj_esp3_1)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen3_id, obj_esp3_2)
            )
            cur.execute(
                "INSERT INTO objetivos_especificos (objetivo_general_id, objetivo_especifico) VALUES (%s, %s)",
                (obj_gen3_id, obj_esp3_3)
            )
            connection.commit()
        
        connection.close()
        
        return redirect(url_for('llenarautodiagnostico'))
    
    mision = session.get('mision', '')  # Obtener la misión de la sesión
    
    return render_template('vistas/crear-unidad-estrategica.html', mision=mision)

@app.route('/llenar-autodiagnostico', methods=['GET', 'POST'])
def llenarautodiagnostico():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        plan_id = session.get('empresa_id')
        
        # Guardar respuestas del cuestionario
        for i in range(1, 26):
            respuesta = request.form.get(f'pregunta{i}')
            if respuesta:
                connection = get_db_connection()
                with connection.cursor() as cur:
                    cur.execute(
                        "INSERT INTO respuestas_autodiagnostico (plan_id, pregunta_num, respuesta) VALUES (%s, %s, %s)",
                        (plan_id, i, respuesta)
                    )
                    connection.commit()
                connection.close()
        
        # Guardar fortalezas
        fortalezas = request.form.getlist('fortalezas[]')
        for fortaleza in fortalezas:
            if fortaleza:
                connection = get_db_connection()
                with connection.cursor() as cur:
                    cur.execute(
                        "INSERT INTO fortalezas (plan_id, fortaleza) VALUES (%s, %s)",
                        (plan_id, fortaleza)
                    )
                    connection.commit()
                connection.close()
        
        # Guardar debilidades
        debilidades = request.form.getlist('debilidades[]')
        for debilidad in debilidades:
            if debilidad:
                connection = get_db_connection()
                with connection.cursor() as cur:
                    cur.execute(
                        "INSERT INTO debilidades (plan_id, debilidad) VALUES (%s, %s)",
                        (plan_id, debilidad)
                    )
                    connection.commit()
                connection.close()
        
        # Guardar resultado del autodiagnóstico
        resultado = calculate_total(request.form)
        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute(
                "UPDATE planes_estrategicos SET resultado_autodiagnostico = %s WHERE id = %s",
                (resultado, plan_id)
            )
            connection.commit()
        connection.close()
        
        return redirect(url_for('inicio'))

    return render_template('vistas/llenar-autodiagnostico.html', preguntas=[
        "La empresa tiene una política sistematizada de cero defectos en la producción de productos/servicios.",
        "La empresa emplea los medios productivos tecnológicamente más avanzados de su sector.",
        "La empresa dispone de un sistema de información y control de gestión eficiente y eficaz.",
        "Los medios técnicos y tecnológicos de la empresa están preparados para competir en un futuro a corto, medio y largo plazo.",
        "La empresa es un referente en su sector en I+D+i.",
        "La excelencia de los procedimientos de la empresa (en ISO, etc.) son una principal fuente de ventaja competitiva.",
        "La empresa dispone de página web, y esta se emplea no sólo como escaparate virtual de productos/servicios, sino también para establecer relaciones con clientes y proveedores.",
        "Los productos/servicios que desarrolla nuestra empresa llevan incorporada una tecnología difícil de imitar.",
        "La empresa es referente en su sector en la optimización, en términos de coste, de su cadena de producción, siendo ésta una de sus principales ventajas competitivas.",
        "La informatización de la empresa es una fuente de ventaja competitiva clara respecto a sus competidores.",
        "Los canales de distribución de la empresa son una importante fuente de ventajas competitivas.",
        "Los productos/servicios de la empresa son altamente, y diferencialmente, valorados por el cliente respecto a nuestros competidores.",
        "La empresa dispone y ejecuta un sistemático plan de marketing y ventas.",
        "La empresa tiene optimizada su gestión financiera.",
        "La empresa busca continuamente mejorar la relación con sus clientes cortando los plazos de ejecución, personalizando la oferta o mejorando las condiciones de entrega. Pero siempre partiendo de un plan previo.",
        "La empresa es referente en su sector en el lanzamiento de innovadores productos y servicios de éxito demostrado en el mercado.",
        "Los Recursos Humanos son especialmente responsables del éxito de la empresa, considerándolos incluso como el principal activo estratégico.",
        "Se tiene una plantilla altamente motivada, que conoce con claridad las metas, objetivos y estrategias de la organización.",
        "La empresa siempre trabaja conforme a una estrategia y objetivos claros.",
        "La gestión del circulante está optimizada.",
        "Se tiene definido claramente el posicionamiento estratégico de todos los productos de la empresa.",
        "Se dispone de una política de marca basada en la reputación que la empresa genera, en la gestión de relación con el cliente y en el posicionamiento estratégico previamente definido.",
        "La cartera de clientes de nuestra empresa está altamente fidelizada, ya que tenemos como principal propósito el deleitarlos día a día.",
        "Nuestra política y equipo de ventas y marketing es una importante ventaja competitiva de nuestra empresa respecto al sector.",
        "El servicio al cliente que prestamos es uno de nuestras principales ventajas competitivas respecto a competidores."
    ])


@app.route('/matriz-crecimiento', methods=['GET', 'POST'])
def matrizcrecimiento():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Aquí puedes manejar la lógica de guardar los datos de la matriz de crecimiento si es necesario
        return redirect(url_for('matrizcrecimiento'))

    return render_template('vistas/matriz-crecimiento.html')

@app.route('/resultado-cuestionario/<int:cuestionario_id>')
def resultado_cuestionario(cuestionario_id):
    connection = get_db_connection()
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM cuestionarios WHERE id = %s", (cuestionario_id,))
        cuestionario = cur.fetchone()
        cur.execute("SELECT * FROM respuestas WHERE plan_id = %s", (cuestionario_id,))
        respuestas = cur.fetchall()
        cur.execute("SELECT * FROM fortalezas WHERE plan_id = %s", (cuestionario_id,))
        fortalezas = cur.fetchall()
        cur.execute("SELECT * FROM debilidades WHERE plan_id = %s", (cuestionario_id,))
        debilidades = cur.fetchall()
    connection.close()
    return render_template('vistas/resultado.html', cuestionario=cuestionario, respuestas=respuestas, fortalezas=fortalezas, debilidades=debilidades)

@app.route('/ver-plan/<int:plan_id>')
def ver_plan(plan_id):
    connection = get_db_connection()
    with connection.cursor() as cur:
        # Obtener el plan
        cur.execute("SELECT * FROM planes_estrategicos WHERE id = %s", (plan_id,))
        plan = cur.fetchone()

        # Obtener los valores
        cur.execute("SELECT * FROM valores WHERE plan_id = %s", (plan_id,))
        valores = cur.fetchall()

        # Obtener los objetivos generales y específicos
        cur.execute("""
            SELECT og.id as objetivo_general_id, og.objetivo_general, oe.id as objetivo_especifico_id, oe.objetivo_especifico
            FROM objetivos_generales og
            LEFT JOIN objetivos_especificos oe ON og.id = oe.objetivo_general_id
            WHERE og.plan_id = %s
        """, (plan_id,))
        rows = cur.fetchall()

        # Agrupar los objetivos específicos bajo cada objetivo general
        objetivos_generales = {}
        for row in rows:
            obj_gen_id = row['objetivo_general_id']
            if obj_gen_id not in objetivos_generales:
                objetivos_generales[obj_gen_id] = {
                    'objetivo_general': row['objetivo_general'],
                    'objetivos_especificos': []
                }
            if row['objetivo_especifico']:
                objetivos_generales[obj_gen_id]['objetivos_especificos'].append({
                    'id': row['objetivo_especifico_id'],
                    'objetivo_especifico': row['objetivo_especifico']
                })

        # Convertir el diccionario en una lista
        objetivos_generales = list(objetivos_generales.values())

        # Obtener las respuestas del autodiagnóstico
        cur.execute("SELECT * FROM respuestas_autodiagnostico WHERE plan_id = %s", (plan_id,))
        respuestas = cur.fetchall()

        # Obtener las fortalezas
        cur.execute("SELECT * FROM fortalezas WHERE plan_id = %s", (plan_id,))
        fortalezas = cur.fetchall()

        # Obtener las debilidades
        cur.execute("SELECT * FROM debilidades WHERE plan_id = %s", (plan_id,))
        debilidades = cur.fetchall()

    connection.close()

    return render_template('vistas/ver_plan.html', plan=plan, valores=valores, objetivos_generales=objetivos_generales, respuestas=respuestas, fortalezas=fortalezas, debilidades=debilidades)


@app.route('/eliminar-plan/<int:plan_id>', methods=['POST'])
def eliminar_plan(plan_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    try:
        with connection.cursor() as cur:
            # Eliminar todos los objetivos específicos relacionados con los objetivos generales del plan
            cur.execute("""
                DELETE objetivos_especificos FROM objetivos_especificos 
                INNER JOIN objetivos_generales ON objetivos_generales.id = objetivos_especificos.objetivo_general_id
                WHERE objetivos_generales.plan_id = %s
            """, (plan_id,))
            
            # Eliminar todos los objetivos generales relacionados con el plan
            cur.execute("DELETE FROM objetivos_generales WHERE plan_id = %s", (plan_id,))
            
            # Eliminar todas las respuestas del autodiagnóstico relacionadas con el plan
            cur.execute("DELETE FROM respuestas_autodiagnostico WHERE plan_id = %s", (plan_id,))
            
            # Eliminar todas las fortalezas relacionadas con el plan
            cur.execute("DELETE FROM fortalezas WHERE plan_id = %s", (plan_id,))
            
            # Eliminar todas las debilidades relacionadas con el plan
            cur.execute("DELETE FROM debilidades WHERE plan_id = %s", (plan_id,))
            
            # Eliminar todos los valores relacionados con el plan
            cur.execute("DELETE FROM valores WHERE plan_id = %s", (plan_id,))
            
            # Finalmente, eliminar el plan estratégico
            cur.execute("DELETE FROM planes_estrategicos WHERE id = %s", (plan_id,))
            
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

    return redirect(url_for('inicio'))






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

@app.route('/contacto/<nombre>/int:edad')
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
