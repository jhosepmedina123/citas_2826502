from . import app, db
from .models import Medico
from .models import Paciente
from .models import Consultorio
from flask import render_template, request, flash, redirect

#------------------------------------------------------------------

@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)

#------------------------------------------------------------------

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

#------------------------------------------------------------------

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

#------------------------------------------------------

@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html", med = medico)

#------------------------------------------------------------------

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html", paci = paciente)

#------------------------------------------------------------------

@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html", consul = consultorio)

#------------------------------------------------------------------

#crear ruta para crear nuevo medico
@app.route("/medicos/create", methods = ['GET' , 'POST'])
def create_medico():
    if( request.method == 'GET' ):
        especialidades = [
            "Cardiologia",
            "Pediatria",
            "Odontologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)
    
    elif(request.method == 'POST'):
        new_medico = Medico(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            numero_identificacion = request.form["n1"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico Registrado correctamente")
        return redirect ("/medicos")
#------------------------------------------------------------------------------------------------

@app.route("/pacientes/create", methods = ['GET' , 'POST'])
def create_paciente():
    if( request.method == 'GET' ):
        return render_template("paciente_form.html")
    elif(request.method == 'POST'):
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["CC"],
                            numero_identificacion = request.form["nd"],
                            altura = request.form["est"],
                            tipo_sangre = request.form["ts"]
                            )
        db.session.add(new_paciente)
        db.session.commit()
        flash("Paciente Registrado correctamente")
        return redirect ("/pacientes")

#-------------------------------------------------------------------------------------------------------------------

@app.route("/consultorio/create", methods = ['GET' , 'POST'])
def create_consultorio():
    if( request.method == 'GET' ):
        return render_template("consultorio_form.html")
    elif(request.method == 'POST'):
        new_consultorio = Consultorio(numero = request.form["nombre"])
        db.session.add(new_consultorio)
        db.session.commit()
        flash("Consultorio Registrado correctamente")
        return redirect("/consultorio")
    
#-------------------------------------------------------------------------------------------------------------------

@app.route("/medicos/update/<int:id>", methods=["POST" , "GET"])
def update_medico(id):
    especialidades = [
            "Cardiologia",
            "Pediatria",
            "Odontologia"
        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                        medico_update = medico_update,
                        especialidades = especialidades )
    elif(request.method == 'POST'):
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["t1"]
        medico_update.numero_identificacion = request.form["n1"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return redirect("/medicos")
#-------------------------------------------------------------------------------------------------------------------
    
@app.route("/pacientes/update/<int:id>", methods=["POST" , "GET"])
def update_paciente(id):
    paciente_update = Paciente.query.get(id)
    if(request.method == "GET"):
        return render_template("paciente_update.html",
                        paciente_update = paciente_update)
    elif(request.method == 'POST'):
        paciente_update.nombre = request.form["nombre"]
        paciente_update.apellidos = request.form["apellidos"]
        paciente_update.tipo_identificacion = request.form["CC"]
        paciente_update.numero_identificacion = request.form["nd"]
        paciente_update.altura = request.form["est"]
        paciente_update.tipo_Sangre = request.form["ts"]
        db.session.commit()
        return "paciente actualizado"
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")
#-------------------------------------------------------------------------------------------------------------------

