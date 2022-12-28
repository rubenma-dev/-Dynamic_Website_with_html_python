from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__) #Archivo que va a arrancar mi aplicacion#

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formulario', methods = ['GET', 'POST'])
def informacion():
    if request.method == 'GET':
        conn = sqlite3.connect('datos.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT correo, comentario FROM mensaje")
        comentarios = cursor.fetchall()
         
        return render_template('comunidad.html', comentarios=comentarios)
    else:
     correo = request.form['correo']
     nombre = request.form['nombre']
     apellido = request.form['apellido']
     direccion = request.form['direccion']
     ciudad = request.form['ciudad']
     comentario = request.form['comentario']

     conn = sqlite3.connect('datos.sqlite')
     cursor = conn.cursor()

     cursor.execute("INSERT INTO mensaje VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % 
                    (correo, nombre, apellido, direccion, ciudad, comentario))
    conn.commit()
    conn.close()

    print("Correo:", correo)
    print("Nombre:", nombre)
    print("apellido:", apellido)
    print("direccion:", direccion)
    print("ciudad:", ciudad)
    print("comentario:", comentario)

    return redirect('comunidad.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca_de_mi.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/herramientas')
def herramientas():
    return render_template('herramientas.html')
    
@app.route('/formulario')
def comunidad():
    return render_template('comunidad.html')
if __name__ == '__main__':
    app.run(debug=True)