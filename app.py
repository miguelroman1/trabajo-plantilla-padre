from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "clave_super_segura"

# Base de datos simulada de usuarios
USUARIOS_REGISTRADOS = {
    'admin@correo.com': {
        'contra': 'Admin123',
        'nombre': 'Admin',
        'fecha_nacimiento': '2008-07-05'
    }
}

# Ruta principal
@app.route("/")
def home():
    return redirect(url_for("inicio"))


# ---------------------- LOGIN ----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('logueado') == True:
        return render_template("inicio.html")

    return render_template("login.html")

@app.route("/validlogin", methods=["GET","POST"])
def validlogin():
    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        contra = request.form.get("contra", "")

        if not correo or not contra:
            flash("Por favor, ingresa tu correo y contraseña.", "error")
        elif correo in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[correo]
            if usuario['contra'] == contra:
                # Guardar sesión
                session['usuario_email'] = correo
                session['usuario'] = usuario['nombre']
                session['logueado'] = True

                return redirect(url_for("inicio"))
            else:
                flash("Contraseña incorrecta.", "error")
        else:
            flash("El correo no está registrado.", "error")
    return render_template("login.html")
# ---------------------- REGISTRO ----------------------
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombreCompleto = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip().lower()
        contra = request.form.get("password", "")
        confirm = request.form.get("confirmar", "")
        fecha = request.form.get("fecha_nacimiento", "")
        genero = request.form.get("genero", "")

        if not nombreCompleto or not correo or not contra or not confirm:
            flash("Por favor, completa todos los campos.", "error")
        elif contra != confirm:
            flash("Las contraseñas no coinciden.", "error")
        elif correo in USUARIOS_REGISTRADOS:
            flash("El correo ya está registrado.", "error")
        else:
            # Registrar usuario
            USUARIOS_REGISTRADOS[correo] = {
                'contra': contra,
                'nombre': nombreCompleto,
                'fecha_nacimiento': fecha,
                'genero': genero
            }
            flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for("login"))

    return render_template("registro.html")


# ---------------------- CERRAR SESIÓN ----------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for("login"))


# ---------------------- PÁGINAS PRINCIPALES ----------------------
@app.route("/inicio")
def inicio():
    info = "Bienvenido a nuestra página. Aquí encontrarás información sobre animales exóticos, vehículos antiguos, maravillas del mundo y más."
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


# ---------------------- MAIN ----------------------
if __name__ == "__main__":
    app.run(debug=True)
