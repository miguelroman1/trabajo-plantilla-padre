from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_super_segura"

# Aquí guardaremos temporalmente los usuarios (simula una base de datos)
usuarios = {}

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo")
        password = request.form.get("password")

        # Verificar si el usuario existe y la contraseña coincide
        if correo in usuarios and usuarios[correo] == password:
            flash("✅ Inicio de sesión exitoso")
            return redirect(url_for("inicio.html"))
        else:
            flash("❌ Usuario o contraseña incorrectos")
            return render_template("login.html", title="Inicio de sesión")

    return render_template("login.html", title="Inicio de sesión")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        password = request.form["password"]
        confirmar = request.form["confirmar"]
        fecha = request.form["fecha_nacimiento"]
        genero = request.form["genero"]

        # Validar contraseñas
        if password != confirmar:
            flash("❌ Las contraseñas no coinciden")
            return render_template("registro", title="Registro")

        # Validar si el usuario ya existe
        if correo in usuarios:
            flash("⚠️ Este correo ya está registrado")
            return render_template("registro", title="Registro")

        # Guardar el usuario
        usuarios[correo] = password
        flash(f"✅ Registro exitoso para {nombre} {apellido}")
        return redirect(url_for("inicio.html"))

    return render_template("registro.html", title="Registro")


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


if __name__ == '__main__':
    app.run(debug=True)
