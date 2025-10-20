from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_super_segura"

usuarios = {}

@app.route("/")
def home():
    return redirect(url_for("registro"))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        correo = request.form.get("correo").lower()
        password = request.form.get("password")
        confirmar = request.form.get("confirmar")
        fecha = request.form.get("fecha_nacimiento")
        genero = request.form.get("genero")

        # Validaciones
        if not nombre or not apellido or not correo or not password:
            flash("Todos los campos obligatorios deben completarse", "danger")
            return redirect(url_for("registro"))

        if password != confirmar:
            flash("Las contraseñas no coinciden", "danger")
            return redirect(url_for("registro"))

        if correo in usuarios:
            flash("Este correo ya está registrado", "warning")
            return redirect(url_for("registro"))

        # Guardar el usuario en el diccionario
        usuarios[correo] = {
            "nombre": nombre,
            "apellido": apellido,
            "password": password,
            "fecha": fecha,
            "genero": genero
        }

        flash(f"¡Bienvenido {nombre} {apellido}! Tu cuenta fue creada exitosamente.", "success")
        return redirect(url_for("inicio"))


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
