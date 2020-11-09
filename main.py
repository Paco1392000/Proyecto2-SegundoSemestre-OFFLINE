from flask import Flask, render_template, url_for, request, make_response, session, redirect, jsonify
from Datos.usuario import Usuario
from Datos.receta import Receta
from Datos.comentario import Comentario
from datetime import datetime
from os import environ
import json
import base64
import csv
import pdfkit
import subprocess
import os

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

app = Flask(__name__)

usuarios = []
app.secret_key = b'supah'
recetas = []
comentarios = []
cont_recetas = 0
cont_usuarios = 4
cont_comentarios = 0
usuario_sesion = ''
usuarios.append(Usuario(0,"Paco", "Silva", 20, "paco_139", "admin"))
usuarios.append(Usuario(1,"Gilgamesh", "Uruk", 25, "gilgamesh_12", "usserprovo1"))
usuarios.append(Usuario(2,"Diarmuid", "UaDuibneh", 21, "diarmuidua_13", "diarmuid"))
usuarios.append(Usuario(3,"Administrador", "Administrador", 20, "admin", "admin"))



def validar_login(user, contrasena):
    global usuario_sesion
    for usuario in usuarios:
        if usuario.usuario == user and usuario.contrasena == contrasena:
            usuario_sesion = usuario.getUsuario()
            print(usuario_sesion)
            return usuario
    return None

def val_usuario(user):
    for usuario in usuarios:
        if usuario.usuario == user:
            return usuario
    return None

def val_rec(nom):
    for receta in recetas:
        if receta.titulo == nom:
            return receta
    return None

@app.route('/receta')
def inicioreceta():
    if 'usuario_logeado' in session:
        return render_template('receta.html', usuario=session['usuario_logeado'], recetas=recetas, comentarios=comentarios)
    return render_template('receta.html', usuario=None, recetas=recetas, comentarios=comentarios)

@app.route('/')
def ini():
    return redirect('login')

@app.route('/usuarios', methods=['SET','GET','POST'])
def iniciousuario():
    if 'usuario_logeado' in session:
        return render_template('usuarios.html', usuario=session['usuario_logeado'], usuarios=usuarios)
    return render_template('/inicio', usuario=None)

@app.route('/comentarios', methods=['GET'])
def inicioComentario():
    if 'usuario_logeado' in session:
        return render_template('incoment.html', usuario=session['usuario_logeado'], coment=comentarios)
    return render_template('/inicio', usuario=None)

@app.route('/comentary/<int:ide>', methods=['GET'])
def comentobtenido(ide):
    global comentarios
    if 'usuario_logeado' in session:
        for i in range(len(comentarios)):
            if ide == comentarios[i].getId():
                
                return render_template('mostcoment.html', usuario=session['usuario_logeado'], coment=comentarios[i])
    return redirect('/inicio')

@app.route('/usuarios/<string:uss>', methods=['GET'])
def inperfil(uss):
    global usuarios
    if 'usuario_logeado' in session:
        for i in range(len(usuarios)):
            if uss == usuarios[i].getUsuario():
                return render_template('perfil.html', usuario=session['usuario_logeado'], use=usuarios[i])
    return redirect('/inicio')

@app.route('/usuarios/<string:uss>', methods=['DELETE'])
def borrarUsuario(uss):
    global usuarios
    for i in range(len(usuarios)):
        if uss == usuarios[i].getUsuario():
            del usuarios[i]
            break
    return {"msg": 'Usuario Eliminado'}

@app.route('/publicaciones/<int:ide>', methods=['DELETE'])
def borrarReceta(ide):
    global recetas
    for i in range(len(recetas)):
        if ide == recetas[i].getId():
            del recetas[i]
            break
    return {"msg": 'Receta Eliminada'}

@app.route('/comentarios/<int:ide>', methods=['DELETE'])
def borrarComentario(ide):
    global comentarios
    for i in range(len(comentarios)):
        if ide == comentarios[i].getId_recet():
            del comentarios[i]
            break
    return {"msg": 'Comentario Eliminado'}

@app.route('/publicaciones')
def iniciopublicaciones():
    if 'usuario_logeado' in session:
        return render_template('public.html', usuario=session['usuario_logeado'], recetas=recetas)
    return render_template('/inicio', usuario=None)

@app.route('/publicaciones/<int:resi>', methods=['GET'])
def publicrec(resi):
    global recetas
    if 'usuario_logeado' in session:
        for i in range(len(recetas)):
            if resi == recetas[i].getId():
                return render_template('mostrareceta.html', usuario=session['usuario_logeado'], recet=recetas[i])
    return redirect('/inicio')

@app.route('/receta/<int:receta_id>')
def receta(receta_id):
    receta_seleccionada = recetas[receta_id]
    if 'usuario_logeado' in session:
        return render_template('recetasel.html', usuario=session['usuario_logeado'], receta=receta_seleccionada, comentarios=comentarios)
    return render_template('recetasel.html', usuario=session['usuario_logeado'], receta=receta_seleccionada, comentarios=comentarios)

@app.route('/inicio')
def home():
    if 'usuario_logeado' in session:
        return render_template('home.html', usuario=session['usuario_logeado'], recetas=recetas)
    return render_template('home.html', usuario=None, recetas=recetas)

@app.route('/lostuser', methods=['POST', 'GET'])
def lostuser():
    if request.method == 'POST':
        ussername = val_usuario(request.form['usuario'])
        if ussername != None:
            return render_template('passre.html', ussername = ussername)
        else:
            return render_template('passre.html', ussername = None)
    return render_template('lostuser.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    error1 = None
    if request.method == 'POST':
        global usuarios, cont_usuarios
        id = cont_usuarios
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        username = request.form['usuario']
        password = request.form['contrasena']
        encontrado = False
        if nombre == '' or apellido == '' or edad == '' or username == '' or password == '':
            return redirect('register')
        for usuario in usuarios:
            if usuario.getUsuario() == username:
                encontrado = True
                break
        if encontrado == True:
            error1 = 'Usuario Repetido'
            return render_template('register.html', error1=error1)
        else:
            nuevo = Usuario(id, nombre, apellido, edad, username, password)
            usuarios.append(nuevo)
            cont_usuarios += 1
            return redirect('login')
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        usuario = validar_login(request.form['usuario'], request.form['contrasena'])
        if usuario != None:
            session['usuario_logeado'] = usuario.usuario
            return redirect('inicio')
        else:
            error = 'Contraseña invalida'
            return render_template('login.html', usuario=None, error=error)
    if 'usuario_logeado' in session:
        return redirect('inicio')
    return render_template('login.html', usuario=None, error=error)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('usuario_logeado', None)
    return redirect('login')

@app.route('/comentario/<int:id_receta>', methods=['POST'])
def coment(id_receta):
    global cont_recetas, comentarios, cont_comentarios, usuario_sesion
    fecha = datetime.utcnow()
    usu_se = usuario_sesion
    datos = request.get_json()
    for i in range(len(recetas)):
        if id_receta == recetas[i].getId():
            if datos['comentario'] == '':
                return {"msg": 'Error'}
            nom = recetas[i].getTitulo()
            comment = Comentario(cont_comentarios, usu_se, id_receta, datos['comentario'], fecha, nom)
            comentarios.append(comment)
            cont_comentarios += 1
            return {"msg": 'Comentario Agregado'}
    return {"msg": 'Error'}

@app.route('/receta/postReceta', methods=['POST'])
def agregarReceta():
    global cont_recetas, comentarios
    datos = request.get_json()
    print(datos)
    if datos['autor'] == '' or datos['titulo'] == '' or datos['resumen'] == '' or datos['ingredientes'] == '' or datos['procedimiento'] == '' or datos['tiempo'] == '' or datos['imagen'] == '':
        return {"msg": 'Error en contenido'}
    receta = Receta(cont_recetas, datos['autor'], datos['titulo'], datos['resumen'], datos['ingredientes'], datos['procedimiento'], datos['tiempo'], datos['imagen'])
    recetas.append(receta)
    cont_recetas += 1
    return {"msg": 'Receta agregada'}

@app.route('/usuarios/<string:nombre>', methods=['PUT'])
def actualizarUsuario(nombre):
    global usuarios
    for i in range(len(usuarios)):
        if nombre == usuarios[i].getUsuario():
            datos = request.get_json()
            usuarios[i].setNombre(datos['nombre'])
            usuarios[i].setApellido(datos['apellido'])
            usuarios[i].setEdad(datos['edad'])
            usuarios[i].setUsuario(datos['usuario'])
            usuarios[i].setContrasena(datos['contrasena'])
            break
    return {"msg": 'Datos Actualizados'}

@app.route('/publicaciones/<int:ide>', methods=['PUT'])
def actualizarReceta(ide):
    global recetas
    for i in range(len(recetas)):
        if ide == recetas[i].getId():
            datos = request.get_json()
            recetas[i].setAutor(datos['aut'])
            recetas[i].setTitulo(datos['tit'])
            recetas[i].setResumen(datos['resu'])
            recetas[i].setIngredientes(datos['ingre'])
            recetas[i].setProcedimiento(datos['proce'])
            recetas[i].setTiempo(datos['temp'])
            recetas[i].setImagen(datos['image'])
            break
    return {"msg": 'Receta Actualizada'}

@app.route('/receta/cargarArchivo', methods=['POST'])
def agregarRecetas():
    global cont_recetas, comentarios
    datos = request.get_json()
    if datos['data'] == '':
        return {"msg": 'Error en contenido'}
    contenido = base64.b64decode(datos['data']).decode('utf-8')
    filas = contenido.splitlines()
    reader = csv.reader(filas, delimiter=',')
    for row in reader:
        receta = Receta(cont_recetas, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        recetas.append(receta)
        cont_recetas += 1
    return {"msg": 'Receta agregada'}
    
@app.route('/reportes', methods=['GET'])
def inicioReportes():
    html = render_template('reportes.html', recetas=recetas, usuarios=usuarios, comentarios=comentarios)
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=report.pdf"
    return response


if __name__ == '__main__':
    app.run(port=5000,debug=True)

