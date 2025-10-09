from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/inicio")
def inicio():
    """Ruta para la página de inicio"""
    info = "Bienvenido a nuestra página. Aquí encontrarás información sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar!"
    return render_template("inicio.html", title="Inicio", info=info)

@app.route("/animales")
def animales():
    """Ruta para la sección de animales exóticos"""
    contenido = "Esta sección está dedicada a las especies más raras y fascinantes del planeta. Conoce sus hábitats, características y esfuerzos de conservación."
    return render_template("animales.html", title="Animales Exóticos", content=contenido)
    
@app.route("/vehiculos")
def vehiculos():
    """Ruta para la sección de vehículos antiguos"""
    contenido = "Un viaje al pasado sobre ruedas. Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template("vehiculos.html", title="Vehículos Antiguos", content=contenido)

@app.route("/maravillas")
def maravillas():
    """Ruta para la sección de vehículos antiguos"""
    contenido = "Un viaje al pasado sobre ruedas. Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template("maravillas.html", title="Vehículos Antiguos", content=contenido)

@app.route("/acerca")
def acerca():
    """Ruta para la sección de vehículos antiguos"""
    contenido = "Un viaje al pasado sobre ruedas. Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template("acerca.html", title="Vehículos Antiguos", content=contenido)

if __name__ == '__main__':
    app.run(debug=True)
