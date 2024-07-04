from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# antes de la peticion
@app.before_request
def before_request():
    print("Antes de la peticion..")

# despues de la peticion
@app.after_request
def after_request(response):
    print("Despues de la peticion..")
    return response

@app.route('/login')
def index():
    # return "<h1>hola</h1>"
    data = {
        'titulo':'Iniciar Sesion',
        'Correo':'Correo electronico',
        'Password':'Contraseña'
    }
    return render_template('login/index.html', data=data)

@app.route('/registrarse')
def registrarse():
    data = {
        'titulo':'Registrate',
        'Nombre':'Nombre',
        'Apellidos':'Apellidos',
        'Correo':'Correo electronico',
        'Password':'Contraseña',
        'PasswordRepeat':'Repite la Contraseña'
    }
    return render_template('login/register.html',data=data)

@app.route('/inicio')
def inicio():
    return render_template('vistas/body/inicio.html')

@app.route('/csv')
def subir_csv():
    return render_template('vistas/body/subir-csv.html')

@app.route('/exportar')
def exportar():
    return render_template('vistas/body/exportar.html')

@app.route('/ajustes')
def ajustes():
    return render_template('vistas/body/ajustes.html')


@app.route('/crear-plan')
def crearplan():
    return render_template('vistas/crear-plan.html')

@app.route('/crear-unidad-estrategica')
def crearunidadestrategica():
    return render_template('vistas/crear-unidad-estrategica.html')

@app.route('/crear-cadena-valor')
def crearcadenavalor():
    return render_template('vistas/crear-cadena-valor.html')

@app.route('/crear-analisis-productos-servicios')
def crearanalisisproductosservicios():
    return render_template('vistas/crear-analisis-productos-servicios.html')

@app.route('/pest')
def pest():
    return render_template('vistas/PEST.html')



@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'nombre': nombre,
        'apellido':'Chambilla',
        'edad' : edad
    }
    return render_template('contacto.html', data=data)

# recuperar parametro a traves de una url
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"
@app.route('/guardar', methods=['POST'])
def guardar_matriz_came():
    if request.method == 'POST':
        # Obtener datos del formulario
        acciones = {
            'C': [
                request.form['accion1'],
                request.form['accion2'],
                request.form['accion3']
            ],
            'A': [
                request.form['accion5'],
                request.form['accion6'],
                request.form['accion7']
            ],
            'M': [
                request.form['accion9'],
                request.form['accion10'],
                request.form['accion11']
            ],
            'E': [
                request.form['accion13'],
                request.form['accion14'],
                request.form['accion15']
            ]
        }

        # Aquí puedes procesar o guardar los datos como prefieras
        # Por ejemplo, imprimir en consola para verificar:
        print("Acciones C:")
        print(acciones['C'])
        print("Acciones A:")
        print(acciones['A'])
        print("Acciones M:")
        print(acciones['M'])
        print("Acciones E:")
        print(acciones['E'])
        
       
def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)
