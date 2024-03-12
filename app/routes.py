from . import app, db
from .models import Medico
from .models import Paciente
from .models import Consultorio
from flask import render_template, request

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

#crear ruta traer al medico por id (get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    #return "Id del medico:" + str(id) 
    #traer el medico por ir utilizando la entidad medico
    medico = Medico.query.get(id)
    #y meterlo a una lista
    return render_template("medico.html", med = medico)

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html", paci = paciente)

@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html", consul = consultorio)

#crear ruta para crear nuevo medico
@app.route("/medicos/create", methods = ['GET' , 'POST'])
def create_medico():
    #mostrar el formulario: metodo GET
    if( request.method == 'GET' ):
        #el usuario ingreso con navegador con hhtps://localost:5000/medicos/create
        especialidades = {
            "Cardiologia",
            "Pediatria",
            "Odontologia"
        }
        return render_template("medico_form.html",
                            especialidades = especialidades)
    elif(request.method == 'POST'):
        #cuadno se presiona "guardar"
        #utilizando el metodo POST
        #return request.form["nombre"] + request.form["apellidos"] + request.form["t1"] + request.form["es"]
        #crear un objeto de tipo medico
        new_medico = Medico(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            numero_identificacion = request.form["n1"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la seccion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado"

##cuando el usuario presiona el boton guardar
#los datos del formulario viajan al server
######## Crear ruta para crear nuevo paciente
@app.route("/pacientes/create")
def create_paciente():
    return render_template("paciente_form.html")