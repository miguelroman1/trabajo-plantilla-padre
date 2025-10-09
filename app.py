from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
@app.route("/inicio")
def inicio():
    """Ruta para l pagina de inicio"""
    info = "Bienvenido a nuestra pagina. Aqui encontraras informacion sobre animales exoticos, vehiculos antiguos, maravillas del mundo y mas. !Explora el mundo superior para empezar¡"
    return render_template("inicio.html", title ="inicio",info=info)

@app.route("/animales-exoticos")
def animales_exoticos():
    """Ruta para la seccion de animales exoticos"""
    contenido = "Esta seccion esta dedicada  a las especies mas raras y facsinantes del planeta. Conoce sus habitats, caracteristicas y esfuerzos de conservacion"
    return render_template("animales.html", title = "Animales Exoticos", content = contenido)
    
@app.route("/vehiculos-antiguos")
def vehiculos_antiguos():
    """Ruta para la seccion de vehiculos antiguos"""
    contenido = "Un viaje al paado sobre ruedas. Explora la historia de los automoviles clasicos, su diseño atemporal y las leyendas detras de ellos"
    return render_template("vehiculos.html", title = "Vehiculos Antiguos", content = contenido)

    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)