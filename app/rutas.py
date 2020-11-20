from app.config import app
from flask import request, jsonify, render_template
from app.api_poni import Api_Poni


@app.route('/')
def Index():
    return render_template('help.html')


@app.route('/burro/login', methods=['POST'])
def login() -> jsonify:
    if request.method == 'POST':
        codalu = request.form["codalu"]
        pass_alu = request.form["pass_alu"]

        poni = Api_Poni()
        datos = poni.login(codalu, pass_alu)
        alumno = poni.data_dict(datos)

        if len(datos) > 0:
            return jsonify({
                "msg": True,
                "alumno": alumno
            })
        return jsonify(
            {
                "msg": False,
                "txt": "no se encuentra registrado"
            }
        )


@app.route('/burro/registro', methods=['POST'])
def register() -> jsonify:
    if request.method == 'POST':
        nomalu = request.form["nomalu"]
        apealu = request.form["apealu"]
        sexo = request.form["sexo"]
        codalu = request.form["codalu"]
        pass_alu = request.form["pass_alu"]
        correo_alu = request.form["correo_alu"]
        direc_alu = request.form["direc_alu"]
        telef_alu = request.form["telef_alu"]

        poni = Api_Poni()
        if not poni.check_register(codalu):
            return jsonify(
                {
                    "msg": False,
                    "txt": "Ya se encuentra registrado"
                }
            )

        alumno = (nomalu, apealu, sexo, codalu, pass_alu, correo_alu, direc_alu, telef_alu)
        poni.register(alumno)
        return jsonify(
           {
                "msg": True,
               "txt": "Registrado correctamente"
            }
        )



#cors para que nuestra api sea consumida desde cualquier dominio
@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true" #para permitir coockies
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE" #metodos permitidos
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

