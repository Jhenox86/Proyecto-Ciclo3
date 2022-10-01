
from fileinput import filename
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime
import os 
from flask import send_from_directory
#Creamos el código de conexión a la base de datos


app= Flask (__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistema'

mysql = MySQL(app)


CARPETA=os.path.join('uploads')
app.config['CARPETA']=CARPETA 

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)


#Pasamos los datos de conexión

@app.route('/')
def homepage():
    cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la tabla tisi_contactos
    cur.execute("SELECT * FROM empleados")

    empleados=cur.fetchall()
    print(empleados)
    mysql.connection.commit() # Confirma la ejecución en el motor de base de datos
    return render_template('index.html',empleados=empleados)

@app.route('/browse')
def browse():
    return render_template('browse.html')
@app.route('/details')
def details():
    return render_template('details.html')
@app.route('/resena')
def resena():
    return render_template('resena.html')
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/entrar')
def entrar():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/create')
def create():
    return render_template('create.html')
@app.route('/destroy/<id>')
def destroy(id):
    cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la tabla 
    
    cur.execute('SELECT imagen FROM empleados WHERE id=%s',id )
    fila=cur.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0] ))  

    cur.execute("DELETE FROM empleados WHERE id=%s",(id))
    mysql.connection.commit()
    print(type(id))


    return redirect('/mostrar')
@app.route("/edit/<id>")
def edit(id):

    cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la 
    cur.execute("SELECT * FROM empleados WHERE id=%s",(id))

    empleados=cur.fetchall()

    mysql.connection.commit() # Confirma la ejecución en el motor de base de datos


    return render_template('edit.html',empleados=empleados)

@app.route('/store', methods=['POST'])
def storage(): # Función para recuperar datos de formulario
    if request.method == 'POST': # Validación de método de envío#Recuperación de datos enviados por el formulario
        _nombre = request.form['txtNombre']
        _correo = request.form['txtCorreo']
        _foto = request.files['txtFoto']
        now=datetime.now()
        tiempo=now.strftime("%Y%H%M%S")
        if _foto.filename!='':
            nuevoNombreFoto=tiempo+_foto.filename
            _foto.save("uploads/"+nuevoNombreFoto)

        #empresa = request.form['empresa']
        #mensaje= request.form['mensaje']
        cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la tabla 
        cur.execute('INSERT INTO empleados(nombre,correo, imagen) VALUES(%s,%s, %s)',(_nombre, _correo,nuevoNombreFoto))
        mysql.connection.commit() # Confirma la ejecución en el motor de base de datos
        return redirect('/resena') #direcciona a contactos#Validamos que sea la función principal
@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    id=request.form['txtID']

    cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la tabla 
    
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename!='':
            nuevoNombreFoto=tiempo+_foto.filename
            _foto.save("uploads/"+nuevoNombreFoto)
            cur.execute('SELECT imagen FROM empleados WHERE id=%s',id )
            fila=cur.fetchall()

            os.remove(os.path.join(app.config['CARPETA'],fila[0][0] ))  
            cur.execute("UPDATE empleados SET imagen=%s WHERE id=%s",(nuevoNombreFoto,id) )
            mysql.connection.commit()


    cur.execute('UPDATE empleados SET nombre=%s,correo=%s WHERE id=%s',(_nombre,_correo, id ) )
    mysql.connection.commit() # Confirma la ejecución en el motor de base de datos
    return redirect('/mostrar')
    

@app.route('/mostrar')
def home():
    cur = mysql.connection.cursor()# Ejecución de consulta de inserción de datos en la tabla 
    cur.execute("SELECT * FROM empleados")

    empleados=cur.fetchall()
    #print(empleados)
    mysql.connection.commit() # Confirma la ejecución en el motor de base de datos

    return render_template('mostrar.html',empleados=empleados)


if __name__ =="__main__":
    app.run(debug=True,port=8000)