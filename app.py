from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "clave_super_segura"

USUARIOS_REGISTRADOS = {
    'admin@correo.com':{
        'contra':'Admin123',
        'nombre':'Admin',
        'fecha_nacimiento':'2008-07-05'
    }
}
@app.route("/")
def home():
    return redirect(url_for("inicio"))

@app.route("/validLogin", methods = ['GET', 'POST'])
def validLogin():
    if request.method == 'POST':
        email = request.form.get('correo','').strip()
        contra  =request.form.get('contra','')
        
        if not email or not contra:
            flash("Por favor ingresa tu correo y contraseña", "error")
        elif email in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[email]
            if usuario['contra'] == contra:
                session['usuario_email'] = email
                session['usuario'] = usuario['nombre']
                session['logueados'] = True

@app.route("/registro", methods=["GET", "POST"])
def registro():
    error = None
    if request.method == "POST":
        nombreCompleto = request.form["nombre"]
        correo = request.form["correo"]
        contra = request.form["password"]
        confirm = request.form["confirar"]
        fecha = request.form["fecha_nacimiento"]
        genero = request.form["genero"]
        
        if contra != confirm:
            error = "la contraseña es incorrecta"
        
        if error != None:
            flash(error)
            return render_template("registro.html")
        else:
            flash(f"registro exitoso")
            return render_template("inicio.html")



    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo").lower()
        password = request.form.get("password")

        if correo in usuarios and usuarios[correo]["password"] == password:
            nombre = usuarios[correo]["nombre"]
            flash(f"¡Bienvenido {nombre}!", "success")
            return redirect(url_for("inicio"))
        else:
            flash("Correo o contraseña incorrectos", "danger")

    return render_template("login.html")

@app.route("/inicio")
def inicio():
    info = "Bienvenido a nuestra página. Aquí encontrarás información sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar!"
    return render_template("inicio.html", title="Inicio", info=info)

@app.route("/animales")
def animales():
    contenido = "Esta sección está dedicada a las especies más raras y fascinantes del planeta. Conoce sus hábitats, características y esfuerzos de conservación."
    return render_template("animales.html", title="Animales Exóticos", content=contenido)

@app.route("/vehiculos")
def vehiculos():
    contenido = "Un viaje al pasado sobre ruedas. Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template("vehiculos.html", title="Vehículos Antiguos", content=contenido)

@app.route("/maravillas")
def maravillas():
    contenido = "Las maravillas del mundo son testimonios impresionantes de la creatividad y la grandeza humana."
    return render_template("maravillas.html", title="Maravillas del Mundo", content=contenido)

@app.route("/acerca")
def acerca():
    contenido = "Somos un equipo apasionado por la historia, la naturaleza y la cultura. En este sitio compartimos información interesante y educativa."
    return render_template("acerca.html", title="Acerca de Nosotros", content=contenido)

if __name__ == "__main__":
    app.run(debug=True)
